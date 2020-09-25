from itertools import combinations_with_replacement
list1=list(input().split())
c=int(list1[1])
list2=list(combinations_with_replacement(list1[0],c))
list3=[]
for i in list2:
    i=sorted(i)
    list3.append(''.join(i))
list3.sort()
for i in list3:
    print(i)
