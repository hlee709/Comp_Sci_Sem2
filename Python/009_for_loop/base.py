x=int(input("Please enter line length: "))
y=input("Do you want vertical or horizontal?: ")
if y == "vertical":
    for c in range(0, x):
        print ("*")
elif y == "horizontal":
    for n in range(0, x):
        print("*", end="")