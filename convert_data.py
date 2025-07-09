from sqlalchemy import Column, Integer, String, DateTime, create_engine
import sqlite3
import pandas as pd
from datetime import datetime
from transaction import Transaction

Base = declarative_base()

engine = create_engine('sqlite:///infor_trans.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

df = pd.read_csv(r"C:\Users\Danibo\Documents\Fraud detection project\archive\Daily Household Transactions.csv")

try:
    for _, row in df.iterrows():

        date_str = str(row["Date"])
        try:
            date_obj = datetime.strptime(date_str, '%d/%m/%Y %H:%M:%S')
        except:
            date_obj = datetime.strptime(date_str, '%d/%m/%Y')

        transaction = Transaction(
            date = date_obj,
            mode=row['Mode'],
            category=row['Category'],
            subcategory=row['Subcategory'],
            note=row['Note'],
            amount=row['Amount'],
            income=row['Income/Expense'],
            currency=row['Currency'],
            
        )
        session.add(transaction)
    session.commit()

except Exception as e:
    session.rollback()
    print("Error:", e)