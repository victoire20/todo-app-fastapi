from pathlib import Path

from sqlmodel import SQLModel, create_engine, Session
from sqlalchemy.orm import sessionmaker

BASE_DIR = Path(__file__).resolve().parent.parent.parent
sqlite_file_name = BASE_DIR / 'test.db'
SQLALCHEMY_DATABASE_URL = f"sqlite:///{sqlite_file_name}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False}
)

TestingSessionLocal = sessionmaker(bind=engine)

def create_db_and_table():
    SQLModel.metadata.create_all(bind=engine)


def override_get_session():
    create_db_and_table()
    connection = engine.connect()
    transaction = connection.begin()

    session = Session(bind=connection)

    try:
        yield session
    finally:
        session.close()
        transaction.rollback()  # 🔥 rollback ici
        connection.close()