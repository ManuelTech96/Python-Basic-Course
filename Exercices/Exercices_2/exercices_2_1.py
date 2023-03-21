#Falta un profesor y los alumnos dan la clase
#Primero se pide el nombre y la edad de los comps que vinieron a clase.

#Declaring a method to return assistant and teacher
def obtain_mates(cant):
    mates = [] #Declaring the list which will keep all the classmates
    
    #Itering times equal to the quantity of mates are in class
    for i in range(cant):
        nombre = input("Ingrese el nombre: ")
        edad = int(input("Ingrese la edad: "))
        mate = (nombre, edad)
        #Adding mate info to the list
        mates.append(mate)
    
    #Sorting the list from younger to older    
    mates.sort(key = lambda x:x[1])
    
    #The once with less age is the asistant and the once with more age is the teacher
    #The firstone and lastone in the list respective
    asistant = mates[0][0]
    teacher = mates[-1][0]
    
    #Returning the assistant and the teacher
    return asistant, teacher

#Unpacking the info from the mates
asistant, teacher = obtain_mates(5)

#Printing info about teacher and assitant
print(f"El profesor es {teacher} y su asistente es {asistant}")