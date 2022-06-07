b = int(input("How many items do you want to buy: "))

total = 0
for x in range(0, b):
    i = input("What item are you buying: ")
    c = float(input("How much does this item cost?: "))
    total = total + c
    print("Thank you for purchasing " + i + "!")
    
print("Your total is: " + str(total))
    



    


