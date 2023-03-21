#creating set with function
conjunto = set(["Data1", "Data2"])

#You only can to put an unhasheable group in an unhasheable group
conjunto2 = set(["Data1", ("data1", "data2")])

#Introducing set in an other set
conjunto3 = frozenset(["dato1", "dato2"]) #Freeze a group making in hasheable
conjunto4 = {conjunto3, "dato3"}

#print(conjunto4)

#Teoria de conjuntos

conjuntoA = {1,3,5,7}
conjuntoB = {1,3,7}

#Verify if its a subset or not
result = conjuntoB.issubset(conjuntoA)

result = conjuntoB <= conjuntoA

#Verify if its a superset or not
result = conjuntoB.issuperset(conjuntoA)
result = conjuntoB > conjuntoA

#Verify if is any number in common
result = conjunto.isdisjoint(conjuntoA)

print(result)