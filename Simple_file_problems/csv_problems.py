import csv
import pandas as pd

#Changing datatype of a col
df = pd.read_csv("Simple_file_problems\\datos.csv")

#Convert all types of a col
# print(type(df["edad"][0]))
# df['edad'] = df['edad'].astype(str)
# print(type(df["edad"][0]))

#replacing data
# df["nombre"].replace("manuel","cortina",inplace=True)
# print(df["nombre"])

#Deleting row where value are empty
# print(df)
# df = df.dropna()
#df = df.dropna(axis=1)
# print(df)

#Deleting repeat rows
# print(df)
# df = df.drop_duplicates()
# print(df)

#Reading a large csv file -> optimu way to
# def read_csv_in_chunks(file_name):
#     for i, chunk in enumerate(pd.read_csv(file_name, chunksize=1000)):
#         print("Chunk #{}".format(i))
#         print(chunk)
        
# read_csv_in_chunks("big_file.csv")

#Reading a large csv file with csv.reader -> optimu way to
# def read_csv_in_chunks(file_name):
#     with open(file_name, 'r') as f:
#         reader = csv.reader(f)
#         header = next(reader)
#         for i, chunk in enumerate(reader):
#             print("Chunk #{}".format(i))
#             print(chunk)
        
# read_csv_in_chunks("big_file.csv")

#Creating a new csv
df.to_csv("Simple_file_problems\\datos_limpios.csv")