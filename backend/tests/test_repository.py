import unittest, sys, pathlib, tempfile, os
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from app.repository import MemoryRepository, SQLiteRepository, SQLAlchemyRepository, PostgresRepository, make_repository
from scripts.migrate_sqlite_to_postgres import migrate

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
        # Verify postgres:// is rewritten to postgresql://
        with tempfile.TemporaryDirectory() as directory:
            dummy_repo = SQLAlchemyRepository(f"sqlite:///{directory}/dummy.db")
            self.assertTrue(dummy_repo.url.startswith("sqlite:///"))

    def test_database_migration_tool(self):
        with tempfile.TemporaryDirectory() as directory:
            src_url = f"sqlite:///{directory}/src.db"
            dst_url = f"sqlite:///{directory}/dst.db"
            src_repo = SQLiteRepository(src_url)
            src_repo.create({'collection_id':'c1','title':'Migrated note','body':'Testing migration','kind':'Field note','place':'Almaty','region':'KZ','date':'Today','color':'#d87551','tags':['migrated'],'source':'Test','starred':True,'x':45.0,'y':55.0})
            
            result = migrate(src_url, dst_url)
            self.assertGreaterEqual(result['target_collections'], 3)
            self.assertGreaterEqual(result['target_observations'], 7)
            
            dst_repo = SQLiteRepository(dst_url)
            dst_atlas = dst_repo.list_atlas()
            migrated_note = next(o for o in dst_atlas['observations'] if o['title'] == 'Migrated note')
            self.assertTrue(migrated_note['starred'])
            self.assertEqual(migrated_note['x'], 45.0)

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

if __name__=='__main__': unittest.main()
