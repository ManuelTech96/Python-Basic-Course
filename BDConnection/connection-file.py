import pyodbc
import pandas as pd

server = 'localhost'
database = 'TurboRenting2'
username = 'sa'
password = 'test1234'
driver = '{ODBC Driver 17 for SQL Server}'

table_names_dict = {}
client_dict = {}
contract_dict = {}
client = 1
contract = 1
t_name = 1

required_tables = ['Clients', 'Contracts', 'Garages', 'Users', 'Vehicules']

conn = pyodbc.connect('Driver='+driver+';Server='+server+';Database='+database+';UID='+username+';PWD='+password)

cursor = conn.cursor()

for row in cursor.tables():
    for name in required_tables:
        if(name == row.table_name):
            table_names_dict[t_name] = f'{row.table_name}'
            t_name += 1

cursor.execute("SELECT * FROM dbo.Clients")

for row in cursor.fetchall():
    chain = f'{row}'
    client_dict[client] = {chain}
    client += 1


cursor.execute("SELECT * FROM dbo.Contracts")
    
for row in cursor.fetchall():
    chain = f'{row}'
    contract_dict[contract] = {chain}
    contract += 1

client_keys = client_dict.keys()
contract_keys = contract_dict.keys()
table_names_keys = table_names_dict.keys()

with open("BDConnection\\data\\data.txt", "w", encoding="UTF-8") as file:
    # x = 0
    # file.writelines(f'{table_names_keys[x]}\n\n')
    
    # for key in client_keys:  
    #     file.writelines(f'{client_dict[key]}\n')
        
    # x += 1
    # file.writelines(f'{table_names_keys[x]}\n\n')
    
    # for key in contract_keys:  
    #     file.writelines(f'{contract_dict[key]}\n')
    
    for key in table_names_keys:
        file.writelines(f'{table_names_dict[key]}\n')
    