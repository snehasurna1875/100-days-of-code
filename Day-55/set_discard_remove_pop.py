n = int(input())
s = set(map(int, input().split()))
N = int(input())

for i in range(0,N):
     a=input().split()
     
     if a[0]=='pop':
        s.pop()
     if a[0]=='remove':
        b=int(a[1])
        s.remove(b)
     if a[0]=='discard':
        b=int(a[1])
        s.discard(b)
    
sum=0
for j in s:
    sum=sum+j
print (sum)