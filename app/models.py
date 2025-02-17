# app/models.py

from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    category = Column(String)
    price = Column(Float)
    quantity = Column(Integer)
    location = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))

    owner = relationship("User", back_populates="products")

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)

    products = relationship("Product", back_populates="owner")

class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey('products.id'))
    buyer_id = Column(Integer, ForeignKey('users.id'))
    quantity = Column(Integer)
    total_price = Column(Float)
    status = Column(String, default="Pending")

    product = relationship("Product")
    buyer = relationship("User")
