import pyodbc as odbc

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

server = 'localhost'
database = 'TurboRenting2'
username = 'sa'
password = 'test1234'
driver = '{ODBC Driver 17 for SQL Server}'

conn = odbc.connect('Driver='+driver+';Server='+server+';Database='+database+';UID='+username+';PWD='+password)

engine = create_engine('Server=DESKTOP-7GBA6AP; Database=TurboRenting2; User Id=sa; Password=test1234')
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()