from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import SessionLocal


async def seed_data():
    """Insert initial seed data for the application using async session."""
    print("🚀 Running seed_data()...")  # ✅ Debug Log

    async with SessionLocal() as db:  # ✅ Use async session
        async with db.begin():  # ✅ Ensure transaction starts
            entities_to_add = [
                {"name": "Organization", "description": "Defines an organization"},
                {"name": "Database", "description": "Defines a database"},
                {"name": "Feature", "description": "Defines a branch"},
            ]