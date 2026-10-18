try : 
    a = float(input("Enter a number : "))
    b = float(input(f"Enter a number to divide {a} : "))
    c = a/b

except ZeroDivisionError :
    print("Divide by 0 is not allowed !")

except ValueError :
    print("Invalid input! Please enter a valid input...")

else :
    print(f"{a} is divided by {b} = {c}")

finally :
    print("End of program")
    print("Made with love by Hemant")