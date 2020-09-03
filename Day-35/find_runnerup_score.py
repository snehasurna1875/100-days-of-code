if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
list1=list(arr)

list1.sort()
for i in range(n-1,-1,-1):
    if list1[n-1]>list1[i] and list1[n-1]!=list1[i] :
        print (list1[i])
        break
