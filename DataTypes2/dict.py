#Creating a dictionary with dict()

diccionario = dict(name="Manuel", surname="Cortina")

#Lists cant be keys cause they are unhasheable at least we use frozenset
diccionario = {frozenset(["Manuel", "Cortina"]): "Programmer"}

#Creating dicctionary with fromkeys() and default value
diccionario = dict.fromkeys(["nombre", "apellido", "edad", "profesion"])

#Creating dicctionary with fromkeys() and changing default value to "unknown"
diccionario = dict.fromkeys(["nombre", "apellido", "edad", "profesion"], "unknown")

print(diccionario)