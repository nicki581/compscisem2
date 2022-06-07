mylist = ["Your mom", "your friend", "your dad", "your teacher", "Your gf"]
compliment = ["is hot", "is pretty", "is nice", "is cool", "is amazing"]

import random
numberpeople= random.randrange(0,len(mylist))
numbercomps= random.randrange(0,len(compliment))

print(mylist[numberpeople]+ " " +compliment[numbercomps])