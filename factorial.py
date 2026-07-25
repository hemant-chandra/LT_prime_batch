n = int(input("Enter a number : "))

def calc_factorial(n) :
    fact =1
    for i in range(1,n+1,1) :
        fact = fact * i
    return fact
print("Factorial of",n,"is :",calc_factorial(n))



