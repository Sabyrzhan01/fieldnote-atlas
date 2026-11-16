from typing import Annotated, Literal
from pydantic import BaseModel, Field, StringConstraints, model_validator

NonBlankTitle = Annotated[str, StringConstraints(strip_whitespace=True, min_length=1, max_length=120)]
NonBlankBody = Annotated[str, StringConstraints(strip_whitespace=True, min_length=1, max_length=1000)]
TagString = Annotated[str, StringConstraints(max_length=40)]
ObservationKind = Literal['Field note', 'Interview', 'Artifact', 'Signal']

class ObservationInput(BaseModel):
    id: str | None = None
    collection_id: str = 'c1'
    title: NonBlankTitle
    body: NonBlankBody
    kind: ObservationKind
    place: str = Field(max_length=160)
    region: str
    date: str
    color: str
    tags: list[TagString] = Field(default_factory=list)
    source: str
    starred: bool = False
    x: float = Field(default=50, ge=0, le=100)
    y: float = Field(default=50, ge=0, le=100)

    latitude: float | None = Field(default=None, ge=-90, le=90)
    longitude: float | None = Field(default=None, ge=-180, le=180)

    @model_validator(mode="after")
    def coordinates_are_paired(self):
        if (self.latitude is None) != (self.longitude is None):
            raise ValueError("Latitude and longitude must be provided together")
        return self

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
