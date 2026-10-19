import unittest, sys, pathlib, tempfile
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from app.repository import MemoryRepository, SQLiteRepository

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

if __name__=='__main__': unittest.main()
