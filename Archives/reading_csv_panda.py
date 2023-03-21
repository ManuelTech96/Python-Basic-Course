import pandas as pd

#using function read_csv to read csv archive
df = pd.read_csv("Archives\\datos.csv")
df2 = pd.read_csv("Archives\\datos.csv")

#Obtaining data from the given column
#print(df["nombre"])

#Itering with sliding given values to set init and ending [x:y]
# chain = "0123456789"
# print(chain[:3])

#Sorting dataframe asc
sorting_df = df.sort_values("edad")

#Sorting dataframe desc
sorting_df_desc = df.sort_values("edad", ascending=False)

#Concating both dataframes
df_concat = pd.concat([df,df2])

#Accesing to first 3 rows with head
first_rows_df = df.head(3)

#Accessing with last 3 rows with tail
last_rows_df = df.tail(3)

#Accesing to row and col count with shape
total_row, total_col = df.shape

#Obtaining stadistic data from data frame
df_info = df.describe()

#Accesing to an especified element of df with loc
selected_element_with_loc = df.loc[2, "edad"]

#Accesing to an especified element of df with iloc
selected_element_with_iloc = df.iloc[2, 2]

#Accesing to all rows of a column
apellidos = df.iloc[:,1]

#Accesign to row 3 with loc
row_3 = df.loc[2,:]

#Accesign to row 3 with loc
row_3 = df.loc[2,:]

#Accesing rows with conditions
more_than_30 = df.loc[df["edad"]<30,:]

print(more_than_30)