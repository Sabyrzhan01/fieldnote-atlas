from pydantic import BaseModel, Field

class ObservationInput(BaseModel):
    collection_id: str = 'c1'
    title: str = Field(min_length=1, max_length=120)
    body: str = Field(min_length=1, max_length=1000)
    kind: str
    place: str = Field(max_length=160)
    region: str
    date: str
    color: str
    tags: list[str] = Field(default_factory=list)
    source: str
    starred: bool = False
    x: float = 50
    y: float = 50

class Observation(ObservationInput):
    id: str

class Collection(BaseModel):
    id: str
    title: str
    subtitle: str
    color: str
    observationCount: int

class AtlasData(BaseModel):
    collections: list[Collection]
    observations: list[Observation]
