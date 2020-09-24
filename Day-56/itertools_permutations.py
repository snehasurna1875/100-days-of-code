from itertools import permutations
b=input().split()
c=int(b[1])
a=tuple(permutations(b[0],c))
listy=[]
for i in a:
    listy.append(''.join(i))
listy.sort()
for i in listy:
    print (i) 