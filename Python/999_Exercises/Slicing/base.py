x=0
y=1
n=input(("whats your first and last name?: "))
for i in range(0,len(n)):
    print(n[x:y])
    x=x+1
    y=y+1
if(n[x:y]==" "):
    print(n[x:len(n)])
    print(n[0:x])

