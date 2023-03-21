import pyodbc
import pandas as pd

server = 'localhost'
database = 'TurboRenting2'
username = 'sa'
password = 'test1234'
driver = 'ODBC Driver 18 for SQL Server'

conn = pyodbc.connect('driver={%s};server=%s;databse=%s;uid=%s;pwd=%s' % (driver, server, database, username, password))

# Query

res = pd.read_sql("SELECT * FROM dbo.Clients c WHERE c.Dni like '71725443N'", con = conn)
res