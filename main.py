from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.api.endpoints import router as api_router
from app.core.seed import seed_data
from app.core.database import engine, Base
from app.core.auth import get_token
from fastapi.middleware.cors import CORSMiddleware


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Lifespan event handler (replaces deprecated on_event)"""
    print("🚀 Running FastAPI lifespan setup...")  # ✅ Debug log

    # Ensure database tables exist
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    print("🚀 Running seed_data()...")  # ✅ Debug log
    # await seed_data()  # ✅ Call properly as async

    yield  # Allow FastAPI to start

    print("🛑 Shutting down FastAPI...")  # ✅ Debug log
    await engine.dispose()

# ✅ Explicitly attach the lifespan event
app = FastAPI(title="Dynamic CRUD API", lifespan=lifespan)



origins = [
    "http://localhost:3000"  # ✅ Example: React frontend
    # "https://yourfrontend.com",  # ✅ Your deployed frontend
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # ✅ Allowed origins
    allow_credentials=True,  # ✅ Allow cookies & authentication headers
    allow_methods=["*"],  # ✅ Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # ✅ Allow all headers
)

# Add token endpoint
app.post("/token")(get_token)

# Register all routers
app.include_router(api_router, prefix="/api/v1")


# ✅ Debug: Ensure lifespan runs
if __name__ == "__main__":
    import uvicorn

    print("🔥 Running FastAPI with lifespan event...")
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)