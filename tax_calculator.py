salary = int(input("Please! Enter your Salary : "))
tax = 0
if (salary < 30000) :
    tax = salary*0.05
    print("You have to pay 5% tax of",salary)
    print("Tax :",tax)
elif (salary >= 30000 and salary <= 70000) :
    tax = salary*0.15
    print("You have to pay 15% tax of",salary)
    print("Tax :",tax)
else :
    tax = salary*0.25
    print("You have to pay 25% of",salary)
    print("Tax :",tax)
    