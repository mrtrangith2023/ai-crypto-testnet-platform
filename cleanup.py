from app.database.database import SessionLocal
from app.models.portfolio_project import PortfolioProject

db = SessionLocal()

deleted = db.query(
    PortfolioProject
).filter(
    PortfolioProject.project_id == 0
).delete()

db.commit()

print(f"Deleted {deleted} records")

db.close()