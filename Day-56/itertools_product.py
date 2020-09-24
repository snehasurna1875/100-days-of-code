from itertools import product
listy1=list(map(int,input().split()))
listy2=list(map(int,input().split()))
a=tuple(product(listy1,listy2))
for i in a:
    print(i,end=" ") 
