# Every for loop while iterate in tuples as well 
# Only iterables elementes can be iterated
animals = ["cat", "dog", "horse", "cow"]

#runing in to animals list
for animal in animals:
    print(f"Now, var is equal to: {animal}")
    
numbers = [1, 2, 3, 4]

#runing in to numbers list and acting above it
for number in numbers:
    result = number * 9
    print(result)
    
#Iterating more than 1 list for each time with zip()
for number,animal in zip(numbers, animals):
    print(f"Running in to list 1: {number}")
    print(f"Running in to list 2: {animal}")

#Iteranting in value set int range()
for num in range(5, 10):
    print(num)
    
#Running in to numbers list by it index (deprecated) [not working in sets]
for num in range(len(numbers)):
    print(numbers[num])
    
#Properly way to iterate a list by it index
for num in enumerate(numbers):
    index = num[0]
    value = num[1]
    print(f"Index: {index} - Value: {value}")

#Most sigma way to iterate a list
for num,i in enumerate(numbers):
    print(f"Index: {num} - Value: {i}")
    
#Using else clause in for loop
for number in numbers:
    print(f"Last loop - Value: {number}")
else:
    print("Loop ending")