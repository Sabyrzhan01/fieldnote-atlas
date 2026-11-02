import unittest, sys, pathlib, tempfile, os
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from app.repository import MemoryRepository, SQLiteRepository, SQLAlchemyRepository, PostgresRepository, make_repository, normalize_db_url
from scripts.migrate_sqlite_to_postgres import migrate
from scripts.seed_db import seed_database

class RepositoryTests(unittest.TestCase):
    def setUp(self): self.repo=MemoryRepository()
    def test_seeded_atlas_contains_collections_and_observations(self):
        atlas=self.repo.list_atlas()
        self.assertGreaterEqual(len(atlas['collections']),3)
        self.assertGreaterEqual(len(atlas['observations']),6)
        self.assertEqual(sum(c['observationCount'] for c in atlas['collections']),len(atlas['observations']))
    def test_create_and_star_observation(self):
        item={'title':'Test note','body':'Something noticed','kind':'Field note','place':'Test place','region':'Almaty','date':'Today','color':'#d87551','tags':['test'],'source':'Walk','starred':False}
        atlas=self.repo.create(item); created=atlas['observations'][0]
        self.assertEqual(created['title'],'Test note')
        toggled=self.repo.toggle_star(created['id'])
        self.assertTrue(next(o for o in toggled['observations'] if o['id']==created['id'])['starred'])
        updated=self.repo.update(created['id'], {**item, 'title': 'Edited note'})
        self.assertEqual(next(o for o in updated['observations'] if o['id']==created['id'])['title'], 'Edited note')
    def test_create_observation_preserves_selected_collection(self):
        item={'collection_id':'c2','title':'Pipe hum','body':'A low pulse at dusk','kind':'Field note','place':'Test place','region':'Almaty','date':'Today','color':'#73937c','tags':[],'source':'Walk','starred':False}
        atlas=self.repo.create(item); created=atlas['observations'][0]
        counts={c['id']:c['observationCount'] for c in atlas['collections']}
        self.assertEqual(created['collection_id'],'c2')
        self.assertEqual(counts['c2'],1)
        self.assertEqual(counts['c1'],6)
    def test_missing_observation_returns_none(self):
        self.assertIsNone(self.repo.toggle_star('missing'))
        self.assertIsNone(self.repo.delete('missing'))
    def test_delete_observation(self):
        item={'title':'Test note','body':'Something noticed','kind':'Field note','place':'Test place','region':'Almaty','date':'Today','color':'#d87551','tags':[],'source':'Walk','starred':False}
        created=self.repo.create(item)['observations'][0]['id']
        self.assertFalse(any(o['id']==created for o in self.repo.delete(created)['observations']))

class SQLiteRepositoryTests(unittest.TestCase):
    def test_sqlalchemy_sqlite_persists_create_and_star(self):
        with tempfile.TemporaryDirectory() as directory:
            url=f"sqlite:///{directory}/atlas.db"
            repo=SQLiteRepository(url)
            created=next(o for o in repo.create({'collection_id':'c2','title':'Night pipe','body':'A steady low hum','kind':'Field note','place':'Canal','region':'Almaty','date':'Today','color':'#73937c','tags':['sound'],'source':'Walk','starred':False,'x':37,'y':62})['observations'] if o['title']=='Night pipe')
            self.assertEqual(created['collection_id'],'c2')
            self.assertEqual(created['x'],37)
            repo.toggle_star(created['id'])
            reopened=SQLiteRepository(url).list_atlas()
            persisted=next(o for o in reopened['observations'] if o['id']==created['id'])
            self.assertTrue(persisted['starred'])
            counts={c['id']:c['observationCount'] for c in reopened['collections']}
            self.assertEqual(counts['c2'],1)

    def test_sqlalchemy_sqlite_delete_and_unknown(self):
        with tempfile.TemporaryDirectory() as directory:
            repo=SQLiteRepository(f"sqlite:///{directory}/atlas.db")
            created=next(o for o in repo.create({'collection_id':'c1','title':'Delete me','body':'Testing','kind':'Field note','place':'Here','region':'Almaty','date':'Today','color':'#d87551','tags':[],'source':'Walk','starred':False})['observations'] if o['title']=='Delete me')
            self.assertIsNotNone(repo.delete(created['id']))
            self.assertIsNone(repo.delete(created['id']))

    def test_postgres_url_normalization(self):
        # Verify postgres:// and postgresql:// are rewritten to postgresql+psycopg://
        self.assertEqual(
            normalize_db_url("postgres://user:pass@localhost:5432/atlas"),
            "postgresql+psycopg://user:pass@localhost:5432/atlas",
        )
        self.assertEqual(
            normalize_db_url("postgresql://user:pass@localhost:5432/atlas"),
            "postgresql+psycopg://user:pass@localhost:5432/atlas",
        )
        with tempfile.TemporaryDirectory() as directory:
            dummy_repo = SQLAlchemyRepository(f"sqlite:///{directory}/dummy.db")
            self.assertTrue(dummy_repo.url.startswith("sqlite:///"))
            dummy_repo.create({
                'collection_id': 'c1',
                'title': 'Temporary observation',
                'body': 'To be reset',
                'kind': 'Field note',
                'place': 'Abay',
                'region': 'Almaty',
                'date': 'Today',
                'color': '#d87551',
                'tags': [],
                'source': 'Walk',
                'starred': False,
            })
            self.assertEqual(len(dummy_repo.list_atlas()['observations']), 7)
            reset_atlas = dummy_repo.reset()
            self.assertEqual(len(reset_atlas['observations']), 6)

    def test_seed_script_idempotent(self):
        with tempfile.TemporaryDirectory() as directory:
            url = f"sqlite:///{directory}/seeded.db"
            res = seed_database(url, force=True)
            self.assertEqual(res['collections'], 3)
            self.assertEqual(res['observations'], 6)

    def test_database_migration_tool(self):
        with tempfile.TemporaryDirectory() as directory:
            src_url = f"sqlite:///{directory}/src.db"
            dst_url = os.environ.get("TEST_POSTGRES_URL") or f"sqlite:///{directory}/dst.db"
            src_repo = SQLiteRepository(src_url)
            # 1. Add a custom observation in collection c2 with custom coordinates and tags
            src_repo.create({
                'collection_id': 'c2',
                'title': 'Migrated canal telemetry',
                'body': 'Testing SQLite to PostgreSQL migration fidelity with custom records',
                'kind': 'Field note',
                'place': 'Esentai River',
                'region': 'Almaty, KZ',
                'date': 'Today',
                'color': '#73937c',
                'tags': ['migrated', 'hydrology'],
                'source': 'Sensor log',
                'starred': True,
                'x': 45.0,
                'y': 55.0
            })
            # 2. Toggle star state on seeded observation #2 (originally unstarred)
            src_repo.toggle_star('2')

            result = migrate(src_url, dst_url)
            self.assertEqual(result['target_collections'], 3)
            self.assertEqual(result['target_observations'], 7)

            dst_repo = SQLAlchemyRepository(dst_url)
            dst_atlas = dst_repo.list_atlas()
            migrated_note = next(o for o in dst_atlas['observations'] if o['title'] == 'Migrated canal telemetry')
            self.assertEqual(migrated_note['collection_id'], 'c2')
            self.assertEqual(migrated_note['place'], 'Esentai River')
            self.assertEqual(migrated_note['tags'], ['migrated', 'hydrology'])
            self.assertTrue(migrated_note['starred'])
            self.assertEqual(migrated_note['x'], 45.0)
            self.assertEqual(migrated_note['y'], 55.0)

            # Verify mutated seed observation #2 preserved its toggled star state
            seed_two = next(o for o in dst_atlas['observations'] if o['id'] == '2')
            self.assertTrue(seed_two['starred'])

            counts = {c['id']: c['observationCount'] for c in dst_atlas['collections']}
            self.assertEqual(counts['c1'], 6)
            self.assertEqual(counts['c2'], 1)

    def test_make_repository_env_detection(self):
        orig_url = os.environ.get('DATABASE_URL')
        try:
            with tempfile.TemporaryDirectory() as directory:
                os.environ['DATABASE_URL'] = f"sqlite:///{directory}/env.db"
                repo = make_repository()
                self.assertIsInstance(repo, SQLAlchemyRepository)
        finally:
            if orig_url is not None:
                os.environ['DATABASE_URL'] = orig_url
            else:
                os.environ.pop('DATABASE_URL', None)

    def test_openapi_observation_input_validation_rejects_invalid_payloads(self):
        from fastapi.testclient import TestClient
        from app.main import app
        client = TestClient(app)
        baseline = {
            'collection_id': 'c1',
            'title': 'Valid observation',
            'body': 'Valid body text',
            'kind': 'Field note',
            'place': 'Abay Ave',
            'region': 'Almaty',
            'date': 'Today',
            'color': '#d87551',
            'tags': ['rain'],
            'source': 'Walk',
            'starred': False,
            'x': 50,
            'y': 50,
        }
        invalid_mutations = [
            {'kind': 'UnknownKind'},
            {'x': -1},
            {'x': 101},
            {'y': -0.5},
            {'y': 100.5},
            {'tags': ['a' * 41]},
            {'title': '   '},
            {'body': '   '},
        ]
        for mod in invalid_mutations:
            resp = client.post('/api/observations', json={**baseline, **mod})
            self.assertEqual(resp.status_code, 422, f"Expected 422 for {mod}, got {resp.status_code}")

if __name__=='__main__': unittest.main()
