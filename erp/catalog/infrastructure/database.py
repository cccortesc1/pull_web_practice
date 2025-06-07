from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def get_engine(db_url="sqlite:///catalog.db"):
    return create_engine(db_url)


def get_session(engine):
    return sessionmaker(bind=engine)
