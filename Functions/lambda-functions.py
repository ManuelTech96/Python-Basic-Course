#Creating lambda function tu get the product of two values
product = lambda x,y : x*y

print(product(3,6))

#creating a common function that said if its par or not par
numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

def is_par(num):
    if(num%2 == 0):
        return  True
    
#using filter with a common function
par_numbers = filter(is_par, numbers)

print(list(par_numbers))

#Creating same function but with lambda function

impar_numbers = filter(lambda number: number%2 == 1, numbers)
print(list(impar_numbers))

