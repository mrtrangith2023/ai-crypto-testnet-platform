from app.database.database import SessionLocal
from app.models.watchlist import Watchlist

db = SessionLocal()

deleted = db.query(
    Watchlist
).delete()

db.commit()

print(f"Deleted {deleted} watchlists")

db.close()