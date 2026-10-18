list = [i*i for i in range(6)]
print(list)


list1 = [i*i for i in range(6) if(i%2 != 0)]
print(list1)

list2 = [-2,3,-4,-5,6,8]
num = [0 if val < 0 else val for val in list2]
print(num)