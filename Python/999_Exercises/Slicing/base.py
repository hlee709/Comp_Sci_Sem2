name = input(str("What is your first name and last name: "))
print(name)
j = 0
k = 1
for i in range(0, len(name)):
    print(name[j:k])
    j += 1
    k += 1

for i in range(0, len(name)):
    y = name[i: i + 1]
    n = " "
    if y==n:
        a = name[i:len(name)]
        b = name[0:i]
        print(a + " " + b)
    
    