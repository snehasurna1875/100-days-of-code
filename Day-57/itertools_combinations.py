from itertools import combinations
b=input().split()
c=int(b[1])
a=()
for i in range(1,(c+1)):
    a=tuple(combinations(b[0],i))
    listy=[]
    x=list(a)
    for i in x:
        listy.append(sorted(i))
    list1=[]
    for i in listy:
      list1.append(''.join(i))
    list1.sort()
    for i in list1:
       print (i) 
