import pyodbc
import pandas as pd

server = 'localhost'
database = 'TurboRenting2'
username = 'sa'
password = 'test1234'
driver = '{ODBC Driver 17 for SQL Server}'

conn = pyodbc.connect('Driver='+driver+';Server='+server+';Database='+database+';UID='+username+';PWD='+password)

pd.read_sql("SELECT * FROM dbo.Clients c WHERE c.Dni like '71725443N'", conn)

# cursor = conn.cursor()

# cursor.execute()

# for row in cursor.fetchall():
#     print(row)