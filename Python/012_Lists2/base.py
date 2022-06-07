x= int(input("How many numbers do you want?"))
thislist= [1,2,3,4,5,6,7,8,9,10]
for i in range(0,x):
    import random
    w= random.randrange(10)
    print(thislist[w])