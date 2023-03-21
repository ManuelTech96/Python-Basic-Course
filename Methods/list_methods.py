#Create a list 
lista = list(["Hi", "Manuel", "How", "Are", "You"])

numeric_list = list([12, 3, 43, 56, True, False, 11, 33])

#Return numbers of elements each list have
elements = len(lista)

#Add element to a list with append
lista.append("?")

#Add element to a list in an especified list
lista.insert(1, ",")

#Add elements to a list
lista.extend([False, 26])

#Delete an element from a list by its index
lista.pop(0)

#To delete elements starting for the end, just give negative index according to the position wanted
lista.pop(-1) #delete the last element of the list

#Remove an element from a list by each value
lista.remove("Manuel") #throw an exception if the value given is not present

#Delete all elements of the list
#lista.clear()

#Sort the elements of a list(not works for strings)
numeric_list.sort() #asc
print(numeric_list)

numeric_list.sort(reverse = True) #desc
print(numeric_list)

#Reverse elements of a list
print(lista)

lista.reverse()

print(lista)
