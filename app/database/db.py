from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def get_database_path(college_name):

    safe_name = (

        college_name
        .lower()
        .replace(" ", "_")
        .replace("/", "_")
    )

    return f"sqlite:///{safe_name}_professors.db"


def get_engine(college_name):

    database_url = get_database_path(
        college_name
    )

    return create_engine(database_url)


def get_session(college_name):

    engine = get_engine(
        college_name
    )

    SessionLocal = sessionmaker(
        bind=engine
    )

    return SessionLocal()