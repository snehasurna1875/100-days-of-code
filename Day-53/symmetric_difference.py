n1=eval(input())
set1=set(map(int,input().split()))
n2=eval(input())
set2=set(map(int,input().split()))
b=set1.symmetric_difference(set2)
listy=list(b)
listy.sort()
for i in listy:
    print(i)