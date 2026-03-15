from app.models import database, db_models
import json

db = next(database.get_db())
chunks = db.query(db_models.ContentChunk).all()
chunk_list = [{"id": c.id, "text": c.text, "metadata": c.metadata_info} for c in chunks]

with open('data/output/extracted_content.json', 'w') as f:
    json.dump(chunk_list, f, indent=4)
