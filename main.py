from fastapi import FastAPI
from app.api import endpoints
from app.models import database, db_models
import uvicorn
import os

# Create DB tables
db_models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="Peblo AI Backend Engineer Challenge", version="1.0.0")

# Include routes
app.include_router(endpoints.router, tags=["Quiz Pipeline"])

@app.get("/")
def read_root():
    return {"message": "Peblo AI Backend Pipeline is running!"}

if __name__ == "__main__":
    # In practice, use a dedicated folder for data
    os.makedirs("data/input", exist_ok=True)
    os.makedirs("data/output", exist_ok=True)
    uvicorn.run(app, host="0.0.0.0", port=8000)
