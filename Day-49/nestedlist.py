listy=[]
name=[]
score=[]
n=eval(input())
if __name__ == '__main__':
    for i in range(n):
        
        listy.append([]) 
            
        listy[i].append(input())
        name.append(listy[i][0])
        listy[i].append(eval(input()))
        score.append(listy[i][1])
name.sort()
score.sort()
max=0
namey=[]


def sorty():
   for i in range(0,n):
    if score[0]<score[i] and score[0]!=score[i]:
       max=score[i]
       return max
y=sorty()
for i in range(n):
     if listy[i][1]==y :
        namey.append(listy[i][0])
namey.sort()
for i in namey:
    print(i)
