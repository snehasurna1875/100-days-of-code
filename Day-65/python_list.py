if __name__ == '__main__':
    N = int(input())
    listy=[]
    for i in range(0,N):
        list1=list(input().split())

        if list1[0]=="insert":
            a=int(list1[1])
            b=int(list1[2])
            listy.insert(a,b)
        if list1[0]=="print":
            print(listy)
        if list1[0]=="remove":
            a=int(list1[1])
            listy.remove(a)
        if list1[0]=="append":
            a=int(list1[1])
            listy.append(a)
        if list1[0]=="sort":
            listy.sort()
        if list1[0]=="pop":
            listy.pop()
        if list1[0]=="reverse":
            listy.reverse()

