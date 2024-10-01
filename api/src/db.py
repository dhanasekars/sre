from dotenv import load_dotenv
import os
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import inspect
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


load_dotenv()
DATABASE_USER = os.getenv("DATABASE_USER")
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")
DATABASE_HOST = os.getenv("DATABASE_HOST")
DATABASE_NAME = os.getenv("DATABASE_NAME")
# DATABASE_URL = f"mysql+aiomysql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}/{DATABASE_NAME}?unix_socket=/tmp/mysql.sock"
DATABASE_URL = f"mysql+aiomysql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}/{DATABASE_NAME}"

# Create async engine
engine = create_async_engine(DATABASE_URL, echo=True)
# Create a session factory for async sessions
SessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine, class_=AsyncSession
)

# Base class for models
Base = declarative_base()


async def check_and_create_tables():
    async with engine.begin() as conn:
        inspector = inspect(conn)
        tables = inspector.get_table_names()

        if 'students' not in tables:
            await conn.run_sync(Base.metadata.create_all)
            logger.info("The 'students' table did not exist and has been created.")
        else:
            logger.info("The 'students' table already exists.")

# Dependency to get a database session
async def get_db():
    async with SessionLocal() as session:
        yield session
