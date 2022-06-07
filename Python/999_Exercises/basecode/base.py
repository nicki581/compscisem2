x=int(input("How many items are you buying today?> "))

total=0
for y in range(0,x):
    i=input("What item are you buying?> ")
    p=float(input("What is the price?> "))
    print("Thank you for purhcasing "+i+"!")
    total=total+p
    
print("Your total is: "+"$"+str(total))

