from sqlalchemy import Column, Integer, String, DateTime, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
import pandas as pd
from datetime import datetime
from transaction import Transaction

Base = declarative_base()

engine = create_engine('sqlite:///infor_trans.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

all_transactions = session.query(Transaction).all()

for one_transaction in all_transactions:
    pass