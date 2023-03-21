import pyodbc

server = 'tcp.myserver.database.windows.net'
database = 'mydb'
username = 'sa'
password = 'test1234'
driver = 'ODBC Driver 18 for SQL Server'

con = pyodbc.connect(f'DRIVER={driver};SERVER={server};DATABASE={database};ENCRYPT=yes;UID={username};PwD={password}')
cursor = con.cursor()