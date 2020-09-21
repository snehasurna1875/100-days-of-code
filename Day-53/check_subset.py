n=eval(input());
for i in range(0,n):
     n1 = int(input())
     arr1 = set(map(int, input().split()))
     n2 = int(input())
     arr2 = set(map(int, input().split()))
     print(arr1.issubset(arr2))
