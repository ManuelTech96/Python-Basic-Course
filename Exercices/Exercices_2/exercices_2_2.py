#Creating a function that verify if given number is prime
def is_prime(num):
    #Verify if given num cant be divided by none number between 2 and given number - 1
    for i in range(2, num-1):
        if num % i == 0:
            #If its divisible return false and end loop 
            return False
        #If loop ends it means it isnt divisible so its prime to return true
        return True
     
#Creating a function that returns all prime numbers from 0 to the given once        
def generating_prime_numbers(num):
    #Creating list
    primes = []
    for i in range(3, num+1):
        #Verifying if value is prime
        result = is_prime(i)
        #f true add it to the list
        if result == True: primes.append(i)
    #Returning the list
    return primes

#Creating the result calling function and print it
result = generating_prime_numbers(123)
print(result)        