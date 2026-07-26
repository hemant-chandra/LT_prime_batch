def even(a,b) :
    for i in range(a,b+1,1) :
        if (i % 2 ==0) :
            print(i)
        else :
            continue
a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
print("Existing even numbers between",a,"to",b,"are :")
even(a,b)