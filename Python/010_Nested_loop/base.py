s = input("What symbol would you like to use: ")
w = int(input("What's the width of your box: "))
h = int(input("What's the height of your box: "))

for c in range(0, h):
    print()
    for n in range(0, w):
        print(s, end='')
    
       