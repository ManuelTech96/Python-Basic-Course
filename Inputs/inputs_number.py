#Ask for a number

#Obtain the numeric chain from the user
number = input("Give a number to duplicate: ")

#Parse it from string to integer
parsed_integer_number = int(number)

#Parse it from string to float
parsed_float_number = float(number)

#Make the operation
integer_duplicate = parsed_integer_number * 2

float_duplicate = parsed_float_number * 2

print(float_duplicate)