if __name__ == '__main__':
    n1 = int(input())
    arr1 = set(map(int, input().split()))
    n2 = int(input())
    arr2 = set(map(int, input().split()))
 

listy=[]
listy=arr1.symmetric_difference(arr2)
print (len(listy))