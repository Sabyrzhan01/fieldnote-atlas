"""Repository implementations. Supports In-Memory, SQLite, and PostgreSQL via SQLAlchemy."""
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
        if not row.get('id'):
            row['id']=str(uuid4())
        row.setdefault('collection_id','c1'); self.observations.insert(0,row); return self.list_atlas()
    def toggle_star(self, item_id):
        for row in self.observations:
            if row['id']==item_id: row['starred']=not row['starred']; return self.list_atlas()
        return None
    def delete(self,item_id):
        before=len(self.observations); self.observations=[o for o in self.observations if o['id']!=item_id]
        return self.list_atlas() if len(self.observations)<before else None

class SQLAlchemyRepository:
    """SQLAlchemy-backed repository supporting SQLite and PostgreSQL."""
    def __init__(self,url: str):
        from sqlalchemy import create_engine, String, Text, Boolean, ForeignKey, JSON, Float
        from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker
        
        # Normalize postgres:// to postgresql:// for SQLAlchemy compatibility
        if url.startswith('postgres://'):
            url = 'postgresql://' + url[len('postgres://'):]
            
        connect_args = {"check_same_thread": False} if url.startswith('sqlite') else {}
        engine_kwargs = {"connect_args": connect_args}
        if not url.startswith('sqlite'):
            engine_kwargs["pool_pre_ping"] = True
            
        engine = create_engine(url, **engine_kwargs)
        
        class Base(DeclarativeBase): pass
        
        class CollectionRow(Base):
            __tablename__ = 'collections'
            id: Mapped[str] = mapped_column(String, primary_key=True)
            title: Mapped[str] = mapped_column(String)
            subtitle: Mapped[str] = mapped_column(String)
            color: Mapped[str] = mapped_column(String)
            
        class ObservationRow(Base):
            __tablename__ = 'observations'
            id: Mapped[str] = mapped_column(String, primary_key=True)
            collection_id: Mapped[str] = mapped_column(ForeignKey('collections.id'))
            title: Mapped[str] = mapped_column(String(120))
            body: Mapped[str] = mapped_column(Text)
            kind: Mapped[str] = mapped_column(String)
            place: Mapped[str] = mapped_column(String)
            region: Mapped[str] = mapped_column(String)
            date: Mapped[str] = mapped_column(String)
            color: Mapped[str] = mapped_column(String)
            tags: Mapped[list] = mapped_column(JSON)
            source: Mapped[str] = mapped_column(String)
            starred: Mapped[bool] = mapped_column(Boolean, default=False)
            x: Mapped[float] = mapped_column(Float, default=50.0)
            y: Mapped[float] = mapped_column(Float, default=50.0)
            
        Base.metadata.create_all(engine)
        self.Session = sessionmaker(engine, expire_on_commit=False)
        self.C = CollectionRow
        self.O = ObservationRow
        self.url = url
        
        with self.Session() as s:
            if not s.get(CollectionRow, 'c1'):
                for c in COLLECTIONS:
                    s.add(CollectionRow(**c))
                for item in seeded():
                    s.add(ObservationRow(**item))
                s.commit()
                
    def list_atlas(self):
        from sqlalchemy import select
        with self.Session() as s:
            collections = []
            for c in s.scalars(select(self.C)).all():
                count = len(s.scalars(select(self.O).where(self.O.collection_id == c.id)).all())
                collections.append({
                    "id": c.id,
                    "title": c.title,
                    "subtitle": c.subtitle,
                    "color": c.color,
                    "observationCount": count
                })
            observations = []
            for o in s.scalars(select(self.O)).all():
                observations.append({
                    "id": o.id,
                    "collection_id": o.collection_id,
                    "title": o.title,
                    "body": o.body,
                    "kind": o.kind,
                    "place": o.place,
                    "region": o.region,
                    "date": o.date,
                    "color": o.color,
                    "tags": o.tags or [],
                    "source": o.source,
                    "starred": bool(o.starred),
                    "x": float(o.x),
                    "y": float(o.y)
                })
            return {"collections": collections, "observations": observations}
            
    def create(self, item):
        from .schemas import ObservationInput
        row = item.model_dump() if isinstance(item, ObservationInput) else dict(item)
        if not row.get('id'):
            row['id'] = str(uuid4())
        row.setdefault('collection_id', 'c1')
        with self.Session() as s:
            s.add(self.O(**row))
            s.commit()
        return self.list_atlas()
        
    def toggle_star(self, item_id):
        with self.Session() as s:
            o = s.get(self.O, item_id)
            if o is None:
                return None
            o.starred = not o.starred
            s.commit()
        return self.list_atlas()
        
    def delete(self, item_id):
        with self.Session() as s:
            o = s.get(self.O, item_id)
            if o is None:
                return None
            s.delete(o)
            s.commit()
        return self.list_atlas()

# Backward-compatible alias
SQLiteRepository = SQLAlchemyRepository
PostgresRepository = SQLAlchemyRepository

def make_repository():
    if os.getenv('FIELDNOTE_REPOSITORY', '').lower() == 'memory':
        return MemoryRepository()
    url = os.getenv('FIELDNOTE_DB_URL') or os.getenv('DATABASE_URL')
    if not url:
        default_db = (Path(__file__).resolve().parents[2] / 'fieldnote-atlas.sqlite3').as_posix()
        url = f'sqlite:///{default_db}'
    return SQLAlchemyRepository(url)
