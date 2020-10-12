#WAP to accept numbers from user and find duplicates
n=list(map(int,input().split()))
count=0
a=[]
a=n
listy=set(a)
list1=list(listy)
for i in range(len(list1)):
    for j in range(len(n)):
      if list1[i]==n[j]:
          count=count+1 
    if count>1 :
        print (list1[i])
