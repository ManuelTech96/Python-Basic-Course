chain1 = "Hi,im,Manuel"
chain2 = "Welcome to python lab"
chain3 = "good morning Sir"

#Turn all characters in upperCase
result = chain1.upper()

#Turn all characters in lowerCase
result = chain2.lower()

#Turn first letter in UpperCase
result = chain3.capitalize()

#Find one chain in another chain. If dont find any coincidence, return -1
find_search = chain1.find("i")

#Find one chain in another chain. If dont find any coincidence, throw an excepcion
find_search = chain1.index("i")

#If numeric, return true, else return false. It doesnt matter if it a string compouse of numbers
is_number = chain1.isnumeric()

#If alphanumeric, return true, else return false. White space count as non alphanumeric char
is_alphanumeric = chain1.isalpha()

#Return number of times a chain cointains each other
characters = chain1.count("Hi")

#Return number of chars a chain contains
string_length = len(chain1)

#Verify if a chain starts with another chain given. If yes, return true, else, return no
starts_with = chain1.startswith("H")

#Verify if a chain ends with another chain given. If yes, return true, else, return no
ends_with = chain1.endswith("l")

#Replace chars of a strings for other given
new_chain1 = chain1.replace("Hi", "Hello")

new_chain2 = chain2.replace("We", "Nosotros")

new_chain3 = chain3.replace(" Sir", ", sir")

new_chain3_2 = new_chain3.capitalize()

#Divide chains with the chain given
breaking_chain = chain1.split(",")

#Add a chain in the result list and move to right the rest of the chain to make sentense Welcome to Jesus python lab
breaking_chain2 = chain2.split(" ")

for chain in breaking_chain2:
    if(chain == "to"):
        position = breaking_chain2.index(chain) + 1
        breaking_chain2.insert(position, "Manuel")

result_chain = ' '.join(breaking_chain2)


print(result_chain)