# SQLAlchemy ka engine banane ke liye
from sqlalchemy import create_engine

# Session (DB connection) manage karne ke liye
from sqlalchemy.orm import sessionmaker, declarative_base


# 🔹 Database connection URL
# SQLite file ka path
DATABASE_URL = "sqlite:///transactions.db"


# 🔹 Engine = actual DB + Python ke beech bridge
engine = create_engine(
    DATABASE_URL,
    # SQLite thread safe issue avoid karne ke liye
    connect_args={"check_same_thread": False}
)


# 🔹 SessionLocal = har request ke liye ek DB session
# autocommit=False → manually commit karenge
# autoflush=False → control hum rakhenge
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


# 🔹 Base class
# Saare SQLAlchemy models isi se inherit honge
Base = declarative_base()


# 🔹 Dependency function (FastAPI ke liye)
# Ye har API request ke liye DB session provide karega
def get_db():
    db = SessionLocal()   # DB connection open
    try:
        yield db          # API ko db session milega
    finally:
        db.close()        # request ke baad DB close
