diccionario = {
    "name": "manuel",
    "surname": "cortina",
    "edad": 26,
    "work": "programmer"
}

#Running a dictionary with items() function to obtain key and values
for data in diccionario.items():
    key = data[0]
    value = data[1]
    print(f"Key: {key} - Value: {value}")