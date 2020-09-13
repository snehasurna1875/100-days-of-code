def average(array):
   setty=set(array) 
   sum=0
   for i in setty:
       sum=sum+i
   ave=sum/len(setty)
   return ave

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)