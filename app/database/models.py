from sqlalchemy import Column, Integer, String, Text, Float
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Professor(Base):

    __tablename__ = "professors"

    id = Column(Integer, primary_key=True)

    college_name = Column(String)

    name = Column(String)

    university = Column(String)

    department = Column(String)

    email = Column(String)

    phone = Column(String)

    profile_url = Column(String)

    resume_url = Column(String)

    linkedin = Column(String)

    scholar = Column(String)

    expertise = Column(Text)

    research_interests = Column(Text)

    summary = Column(Text)

    resume_text = Column(Text)

    score = Column(Float)