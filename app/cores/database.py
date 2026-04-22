import os.path
from pathlib import Path
from typing import Annotated

from fastapi import Depends
from sqlalchemy import create_engine
from sqlmodel import SQLModel, Session

BASE_DIR = Path(__file__).resolve().parent.parent.parent
sqlite_file_name = BASE_DIR / 'database.db'
sql_url = f"sqlite:///{sqlite_file_name}"

connect_args = {'check_same_thread': False}
engine = create_engine(sql_url, connect_args=connect_args)


def create_db_and_table():
    SQLModel.metadata.create_all(bind=engine)


def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]