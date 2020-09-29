n=int(input())
for i in range(0,n): 
    number=list(input().split())
    a=number[0]
    b=number[1]
    try:
      print (int(a)//int(b))
      
    except ZeroDivisionError as e:
      print ("Error Code:",e)
    except ValueError as d:
      print("Error Code:",d)