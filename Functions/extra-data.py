#Creating a function with 3 parameters
# def phrase(name, surname, adjective):
#     return f"Hi {name} {surname}, you are {adjective}"

#Using keyword arguments
# result_phrase = phrase(adjective="awesome", name="Manuel", surname="Cortina")
# print(result_phrase)

#Overwriting optional args
def phrase(name, surname, adjective = "fat"):
    return f"Hi {name} {surname}, you are {adjective}"

result_phrase = phrase("Manuel", "Cortina", adjective="awesome")
print(result_phrase)