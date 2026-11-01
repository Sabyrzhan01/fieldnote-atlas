"""Launch the canonical FastAPI + SQLAlchemy (SQLite/PostgreSQL) application."""
import os
import uvicorn

if __name__ == '__main__':
    host = os.environ.get('HOST', '0.0.0.0')
    port = int(os.environ.get('PORT', 8091))
    uvicorn.run('backend.app.main:app', host=host, port=port, reload=False)
