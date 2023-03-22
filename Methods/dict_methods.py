diccionario = {
    "nombre": 'Manuel',
    "apellido": 'Cortina',
    "edad": 26,
    "trabajo": True
}

#Return an object dict_item (can be iterated)
claves = diccionario.keys()

#Return the value by its key and return none while key or value not in dictionary
valor = diccionario.get("nombre")

#Delete all the elements in the dictionary
#diccionario.clear()

#Delete an especified element from the dictionary
diccionario.pop("apellido")

#Return an iterable dict_item element
iterable_dict = diccionario.items()

print(iterable_dict)