fruits = ["apple", "pear", "cherry", "pineapple", "coconout", "watermelon", "bannana", "raspberry", "blueberry"]

#properly way to aboid the element or elementes than match the if codition by continue clause which break that loop run
for fruit in fruits:
    if fruit == "coconout":
        continue
    print(f"Im gonna eat some {fruit}")
    
print("-----------")

#Avoiding the loop execute
for fruit in fruits:
    if fruit == "pear":
        break
    print(f"Im gonna eat some {fruit}")
    
print("-----------")

#iterating a string
chain = "Hola manuel"

for char in chain:
    print(char)
    
#iterating in one line
bitcoins = [1, 2, 4, 64]

duplicate_bitcoins = [x** x for x in bitcoins]

print(duplicate_bitcoins)

# for bit in bitcoins:
#     duplicate_bitcoins.append(bit*2)

# print(duplicate_bitcoins) 


