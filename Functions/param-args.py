#Not optimus way to sum values
# def suma(number_list):
#     final_number = 0
#     for number in number_list:
#         final_number = final_number = number
#     return final_number
# result = suma([5, 3, 9])
# print(result)

#Optimun way to sum values
def total_sum(numbers):
    return sum([*numbers])

result2 = total_sum([4,5,6,7,9])

print(result2)

#Optimun way to sum values but using args parameter
def suma(name, *numbers):
    return f"Hi {name}, your numbers sum is {sum(numbers)}"

result = suma("Manuel",4,5,6,7,9)

print(result)

