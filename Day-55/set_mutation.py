n=int(input())
set1=set(map(int,input().split()))
N=int(input())

for i in range(0,N):
    a=input().split()
    set2=set(map(int,input().split()))
    if a[0]=='intersection_update' :
        b=int(a[1])
        set1.intersection_update(set2)
    if a[0]=='symmetric_difference_update' :
        b=int(a[1])
        set1.symmetric_difference_update(set2)
    if a[0]=='difference_update':
        b=int(a[1])
        set1.difference_update(set2)
    if a[0]=='update':
        b=int(a[1])
        set1.update(set2)
sum=0
for i in set1:
    sum=sum+i
print (sum)