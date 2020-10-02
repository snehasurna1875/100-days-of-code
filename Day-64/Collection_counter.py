from collections import Counter  
from collections import Counter  
n=int(input())
listy=list(map(int,input().split()))
b=Counter(listy)
q=int(input())
sumy=0
kill=0
z=0

for j in range(0,q):
    
    list1=list(map(int,input().split())) 
    for k in b:
        

        if list1[0]==k:
           
            z=1
         
            if b[k]!=0:
              b[k]=b[k]-1
             
            
              
              sumy=sumy+list1[1]
              
        if z==1 :
         continue
print(sumy)
