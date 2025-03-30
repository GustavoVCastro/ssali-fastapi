from fastapi import FastAPI
from contextlib import asynccontextmanager

from src.books.routes import book_router
from src.db.main import init_db


@asynccontextmanager
async def life_span(app: FastAPI):
    await init_db()
    print(f"server is starting...")
    yield
    print(f"server has been stopped")


version = "v1"

app = FastAPI(
    title="Books",
    description="A REST API for a book review web service",
    version=version,
    lifespan=life_span,
)

app.include_router(book_router, prefix="/api/{version}/books", tags=["books"])
