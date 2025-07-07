from sqlalchemy import Column, Integer, String, DateTime, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
import pandas as pd
from datetime import datetime

Base = declarative_base()

class Transaction(Base):
    __tablename__ = "Transactions"

    id = Column(Integer, primary_key = True)
    date = Column(DateTime)
    mode = Column(String)
    category = Column(String)
    subcategory = Column(String)
    note = Column(String)
    amount = Column(Integer)
    income = Column(String)
    currency = Column(String)