import random
word_list=[]
with open('allow_words.txt') as f:
    for line in f:
        l = line.strip()
        word_list.append(l)


num=random.randrange(0,12972)
answer=word_list[num]
print(answer)

a=0
for i in range(0,6):
    guess = input("Guss a word. ")
    if guess==answer:
        print("u win")
        a=1
        break
    else:
        print("wrong guess again")
        
if a==0:       
    print("loser the answer was "+answer)

f.close()
