#Creating a function to shown fibonaccis sequence from 0 to given number

def fibonacci(num):
    a,b = 0,1
    fibonacci_list = [0]
    
    for i in range(num):
        if b > num: return fibonacci_list
        else:
            fibonacci_list.append(b)
            a,b = b,a+b
            
result = fibonacci(34)
print(result)
            