from fastapi import FastAPI
from routes import base, data
from contextlib import asynccontextmanager
from motor.motor_asyncio import AsyncIOMotorClient
from helpers.config import get_settings

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup code
    settings = get_settings()
    
    # Initialize MongoDB connection
    app.mongo_connection = AsyncIOMotorClient(settings.MONGODB_URL)
    app.db_client = app.mongo_connection[settings.MONGODB_DATABASE]
    
    print("Connected to MongoDB!")
    
    yield  # This separates startup from shutdown code
    
    # Shutdown code
    app.mongo_connection.close()
    print("Closed MongoDB connection!")

app = FastAPI(lifespan=lifespan)

app.include_router(base.base_router)
app.include_router(data.data_router)