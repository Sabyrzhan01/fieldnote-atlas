import os
from pathlib import Path
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from .repository import make_repository
from .schemas import AtlasData, ObservationInput

app = FastAPI(title='Fieldnote Atlas API', version='1.0.0')
app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:5173', 'http://127.0.0.1:5173', 'http://localhost:8000', 'http://127.0.0.1:8000'],
    allow_methods=['*'],
    allow_headers=['*'],
)
repository = make_repository()


@app.get('/api/health')
def health():
    return {'status': 'ok'}


@app.get('/api/atlas', response_model=AtlasData)
def atlas():
    return repository.list_atlas()


@app.post('/api/observations', response_model=AtlasData, status_code=201)
def create_observation(payload: ObservationInput):
    if payload.collection_id not in {c['id'] for c in repository.list_atlas()['collections']}:
        raise HTTPException(status_code=422, detail='Unknown collection')
    return repository.create(payload)


@app.post('/api/observations/{observation_id}/star', response_model=AtlasData)
def toggle_star(observation_id: str):
    result = repository.toggle_star(observation_id)
    if result is None:
        raise HTTPException(status_code=404, detail='Observation not found')
    return result


@app.delete('/api/observations/{observation_id}', response_model=AtlasData)
def delete_observation(observation_id: str):
    result = repository.delete(observation_id)
    if result is None:
        raise HTTPException(status_code=404, detail='Observation not found')
    return result


@app.post('/api/test/reset', response_model=AtlasData)
def reset_database_for_tests():
    if os.environ.get('ENABLE_TEST_RESET') != '1':
        raise HTTPException(status_code=403, detail='Test reset endpoint is disabled')
    return repository.reset()


PROJECT_ROOT = Path(__file__).resolve().parents[2]
DIST_DIR = PROJECT_ROOT / 'frontend' / 'dist'
FRONTEND_DIR = PROJECT_ROOT / 'frontend'
WEB_ROOT = DIST_DIR if DIST_DIR.is_dir() else FRONTEND_DIR

if (WEB_ROOT / 'assets').is_dir():
    app.mount('/assets', StaticFiles(directory=WEB_ROOT / 'assets'), name='assets')


@app.get('/{full_path:path}', include_in_schema=False)
def serve_spa(full_path: str):
    if full_path.startswith('api/'):
        raise HTTPException(status_code=404, detail='Not found')
    candidate = (WEB_ROOT / full_path).resolve()
    if full_path and candidate.is_file() and str(candidate).startswith(str(WEB_ROOT.resolve())):
        return FileResponse(candidate)
    return FileResponse(WEB_ROOT / 'index.html')
