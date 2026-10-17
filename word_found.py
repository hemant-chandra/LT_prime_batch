data = True
word = "Tony"
line = 1

with open("sample.txt", "r") as f :

    while data :
        data = f.readline()
        if word in data : 
            print(f"{word} found in line {line}")
            break
        line += 1
