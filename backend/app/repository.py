"""Repository implementations. SQLite/SQLAlchemy is the default; set FIELDNOTE_DB_URL to override it."""
import os
from pathlib import Path
from copy import deepcopy
from uuid import uuid4
from .seed import COLLECTIONS, seeded

class MemoryRepository:
    def __init__(self):
        self.collections=deepcopy(COLLECTIONS); self.observations=seeded()
    def list_atlas(self):
        collections=deepcopy(self.collections)
        for c in collections: c['observationCount']=sum(o.get('collection_id','c1')==c['id'] for o in self.observations)
        return {"collections":collections,"observations":deepcopy(self.observations)}
    def create(self, item):
        row=item.model_dump() if hasattr(item,'model_dump') else dict(item)
        row['id']=str(uuid4()); row.setdefault('collection_id','c1'); self.observations.insert(0,row); return self.list_atlas()
    def toggle_star(self, item_id):
        for row in self.observations:
            if row['id']==item_id: row['starred']=not row['starred']; return self.list_atlas()
        return None
    def delete(self,item_id):
        before=len(self.observations); self.observations=[o for o in self.observations if o['id']!=item_id]
        return self.list_atlas() if len(self.observations)<before else None

class SQLiteRepository:
    def __init__(self,url):
        from sqlalchemy import create_engine, String, Text, Boolean, ForeignKey, JSON, select
        from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker
        self.sa=(create_engine,String,Text,Boolean,ForeignKey,JSON,select,DeclarativeBase,Mapped,mapped_column,sessionmaker)
        engine=create_engine(url,connect_args={"check_same_thread":False} if url.startswith('sqlite') else {})
        class Base(DeclarativeBase): pass
        class CollectionRow(Base):
            __tablename__='collections'
            id:Mapped[str]=mapped_column(String,primary_key=True); title:Mapped[str]=mapped_column(String); subtitle:Mapped[str]=mapped_column(String); color:Mapped[str]=mapped_column(String)
        class ObservationRow(Base):
            __tablename__='observations'
            id:Mapped[str]=mapped_column(String,primary_key=True); collection_id:Mapped[str]=mapped_column(ForeignKey('collections.id')); title:Mapped[str]=mapped_column(String(120)); body:Mapped[str]=mapped_column(Text); kind:Mapped[str]=mapped_column(String); place:Mapped[str]=mapped_column(String); region:Mapped[str]=mapped_column(String); date:Mapped[str]=mapped_column(String); color:Mapped[str]=mapped_column(String); tags:Mapped[list]=mapped_column(JSON); source:Mapped[str]=mapped_column(String); starred:Mapped[bool]=mapped_column(Boolean,default=False); x:Mapped[float]=mapped_column(default=50); y:Mapped[float]=mapped_column(default=50)
        Base.metadata.create_all(engine); self.Session=sessionmaker(engine,expire_on_commit=False); self.C=CollectionRow; self.O=ObservationRow
        with self.Session() as s:
            if not s.get(CollectionRow,'c1'):
                for c in COLLECTIONS:s.add(CollectionRow(**c))
                for item in seeded():s.add(ObservationRow(**item))
                s.commit()
    def list_atlas(self):
        with self.Session() as s:
            collections=[]
            for c in s.scalars(self.sa[6](self.C)).all():
                collections.append({"id":c.id,"title":c.title,"subtitle":c.subtitle,"color":c.color,"observationCount":len(s.scalars(self.sa[6](self.O).where(self.O.collection_id==c.id)).all())})
            observations=[]
            for o in s.scalars(self.sa[6](self.O)).all(): observations.append({"id":o.id,"collection_id":o.collection_id,"title":o.title,"body":o.body,"kind":o.kind,"place":o.place,"region":o.region,"date":o.date,"color":o.color,"tags":o.tags,"source":o.source,"starred":o.starred,"x":o.x,"y":o.y})
            return {"collections":collections,"observations":observations}
    def create(self,item):
        from .schemas import ObservationInput
        row=item.model_dump() if isinstance(item,ObservationInput) else dict(item); row['id']=str(uuid4()); row.setdefault('collection_id','c1')
        with self.Session() as s:s.add(self.O(**row));s.commit()
        return self.list_atlas()
    def toggle_star(self,item_id):
        with self.Session() as s:
            o=s.get(self.O,item_id)
            if o is None:return None
            o.starred=not o.starred;s.commit()
        return self.list_atlas()
    def delete(self,item_id):
        with self.Session() as s:
            o=s.get(self.O,item_id)
            if o is None:return None
            s.delete(o);s.commit()
        return self.list_atlas()

def make_repository():
    if os.getenv('FIELDNOTE_REPOSITORY','sqlite').lower() == 'memory':
        return MemoryRepository()
    default_db=(Path(__file__).resolve().parents[2]/'fieldnote-atlas.sqlite3').as_posix()
    url=os.getenv('FIELDNOTE_DB_URL') or f'sqlite:///{default_db}'
    return SQLiteRepository(url)
