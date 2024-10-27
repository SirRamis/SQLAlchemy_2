from sqlalchemy import Column, Integer, String, Text, BigInteger, Date, ForeignKey, LargeBinary
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Provider(Base):
    __tablename__ = 'provider'

    id_provider = Column(Integer, primary_key=True, autoincrement=True)
    name_of_provider = Column(String(50), nullable=False)
    representative = Column(Text, nullable=False)
    speak_to = Column(Text, nullable=False)
    phone = Column(String(15), nullable=False)  # Изменили на VARCHAR для поддержки нечисловых символов
    address = Column(Text, nullable=False)

    supplies = relationship("Supply", back_populates="provider", cascade="all, delete")


class Supply(Base):
    __tablename__ = 'supply'

    id_supply = Column(Integer, primary_key=True, autoincrement=True)
    id_provider = Column(Integer, ForeignKey('provider.id_provider', ondelete="CASCADE"))
    data_of_supply = Column(Date, nullable=False)

    provider = relationship("Provider", back_populates="supplies")
    products = relationship("Product", back_populates="supply", cascade="all, delete")


class Product(Base):
    __tablename__ = 'products'

    id_product = Column(Integer, primary_key=True, autoincrement=True)
    id_supply = Column(Integer, ForeignKey('supply.id_supply', ondelete="CASCADE"))
    name_of_product = Column(Text, nullable=False)
    specification = Column(Text)
    description = Column(Text)
    image = Column(LargeBinary)  # BYTEA в PostgreSQL соответствует LargeBinary в SQLAlchemy
    purchase_cost = Column(Integer)
    availability = Column(Integer)
    quantity = Column(Integer)
    selling_price = Column(Integer)

    supply = relationship("Supply", back_populates="products")
    orders = relationship("Order", back_populates="product", cascade="all, delete")


class Employee(Base):
    __tablename__ = 'employees'

    id_employee = Column(Integer, primary_key=True, autoincrement=True)
    family = Column(String(50), nullable=False)
    name = Column(String(50), nullable=False)
    surname = Column(String(50), nullable=False)
    job_title = Column(Integer)  # Тип job_title предполагается как Integer (возможно, связанный с другой таблицей должностей)
    address = Column(Text, nullable=False)
    home_phone = Column(String(15), nullable=False)  # Изменили на VARCHAR для поддержания формата телефонов
    birthday = Column(Date, nullable=False)

    orders = relationship("Order", back_populates="employee", cascade="all, delete")


class Client(Base):
    __tablename__ = 'client'

    id_client = Column(Integer, primary_key=True, autoincrement=True)
    full_name = Column(String(50), nullable=False)
    address = Column(Text, nullable=False)
    phone = Column(String(15), nullable=False)

    orders = relationship("Order", back_populates="client", cascade="all, delete")


class Order(Base):
    __tablename__ = 'orders'

    id_order = Column(Integer, primary_key=True, autoincrement=True)
    id_employee = Column(Integer, ForeignKey('employees.id_employee', ondelete="SET NULL"))
    id_product = Column(Integer, ForeignKey('products.id_product', ondelete="CASCADE"))
    id_client = Column(Integer, ForeignKey('client.id_client', ondelete="SET NULL"))
    posting_date = Column(Date)
    execution_date = Column(Date)

    employee = relationship("Employee", back_populates="orders")
    product = relationship("Product", back_populates="orders")
    client = relationship("Client", back_populates="orders")
