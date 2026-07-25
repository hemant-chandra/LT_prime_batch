word = input("Enter a String : ")
i = 0
v_count = 0
c_count = 0
for i in word :
    if (i == "a" or i == "e" or i == "i" or i == "o" or i == "u" or i == "A" or i == "E" or i == "I" or i == "O" or i == "U") :
        v_count+=1
    elif (i == " ") :
        continue
    else :
        c_count+=1
print("Entered String :",word)
print("There is the count : ")
print("No. of Vovels :",v_count)
print("No. of Consonents :",c_count)
