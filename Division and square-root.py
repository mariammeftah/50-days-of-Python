#Division and square-root
#write a function called divide_or_square that takes one argument (a number) and returns the square root of the number if it is divisible by 5, 
#returns it's remainder if its not divisible by 5. For example, if you pass 10 as an argument, then your function should return 3.16 
#as the squarefoot

def divide_or_square(num):
    if num % 5 == 0 : 
        sqrt = num ** 0.5 # you divide 2 times by 0.5 
        return sqrt    
    else:
       remainder = num % 5
       return remainder

print(divide_or_square(9))
