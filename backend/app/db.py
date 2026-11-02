
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from config import DATABASE_URL
from sqlalchemy.pool import NullPool


# Standard sync engine
engine = create_engine(
    DATABASE_URL,
    connect_args={"prepare_threshold": None},  # psycopg v3: no prepared statements (pooler-safe)
    poolclass=NullPool,                        # the Supabase pooler already pools connections
)

SessionLocal = sessionmaker(bind=engine, expire_on_commit=False)
Base = declarative_base()

#sync initialization
def init_db():
    import models
    Base.metadata.create_all(bind=engine)

#Standard sync generator
def get_db():
    with SessionLocal() as session:
        yield session