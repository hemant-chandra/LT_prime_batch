word = input("Enter a String : ")
i=0
count = 0
alpha = input("Please enter a alphabate, Do you want to find the count : ")
for i in word :
    if alpha == i :
        count = count + 1
print("'",alpha,"'","came",count,"times in this String")

