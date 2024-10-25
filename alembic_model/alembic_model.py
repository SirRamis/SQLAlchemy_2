from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Employee(Base):
    __tablename__ = 'employees'

    id_employee = Column(Integer, primary_key=True)
    family = Column(String(50), nullable=False)
    name = Column(String(50), nullable=False)
    surname = Column(String(50), nullable=False)
    job_title = Column(Integer)
    address = Column(String, nullable=False)
    home_phone = Column(Integer, nullable=False)
    birthday = Column(String, nullable=False)
