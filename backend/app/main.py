from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pathlib import Path
from .repository import make_repository
from .schemas import AtlasData, ObservationInput

app=FastAPI(title='Fieldnote Atlas API',version='1.0.0')
app.add_middleware(CORSMiddleware,allow_origins=['http://localhost:5173','http://127.0.0.1:5173'],allow_methods=['*'],allow_headers=['*'])
repository=make_repository()
@app.get('/api/health')
def health(): return {'status':'ok'}
@app.get('/api/atlas',response_model=AtlasData)
def atlas(): return repository.list_atlas()
@app.post('/api/observations',response_model=AtlasData,status_code=201)
def create_observation(payload:ObservationInput):
    if payload.collection_id not in {c['id'] for c in repository.list_atlas()['collections']}:
        raise HTTPException(status_code=422,detail='Unknown collection')
    return repository.create(payload)
@app.post('/api/observations/{observation_id}/star',response_model=AtlasData)
def toggle_star(observation_id:str):
    result=repository.toggle_star(observation_id)
    if result is None: raise HTTPException(status_code=404,detail='Observation not found')
    return result
@app.delete('/api/observations/{observation_id}',response_model=AtlasData)
def delete_observation(observation_id:str):
    result=repository.delete(observation_id)
    if result is None: raise HTTPException(status_code=404,detail='Observation not found')
    return result

# The root vanilla frontend is canonical. Serve it from the same FastAPI
# process so its /api requests always hit the SQLAlchemy-backed app above.
WEB_ROOT = Path(__file__).resolve().parents[2]
app.mount('/', StaticFiles(directory=WEB_ROOT, html=True), name='web')
