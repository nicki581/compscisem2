x=int(input("Enter line length: "))
y=(input("Vertical or horizantal: "))
w=(input("Enter symbol: "))
v="vertical"
h="horizantal"

if y==v:
    for k in range(0,x):
        print(w)
elif y==h:
    for q in range(0,x):
        print((w),end="")