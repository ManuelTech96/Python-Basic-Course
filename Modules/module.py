#Importing modules and giving them custom name
#import module_say_hi as _say_hi

#Importing all methods of a module -> Not correct form, not optimum at all, discouraged by pp8
#from module_say_hi import *

#Importing just a function from a module and giving them a custom name
#from module_say_hi import saludar as _s

#Importing just a function from a module
from Good_modules.say_hi import saludar, saludar_raro

#Creating variables with greattings
saludo = saludar("Manuel")
saludo_raro = saludar_raro("Pelayo")

#Showing the results
print(saludo)
print(saludo_raro)


#To see namespace module methods
#print(dir(module_say_hi))
