'''WAP to create a list with five numbers and display the following 
1)the reverse of list without using built in function
2)sum of digits in the list
'''
list1=[1,2,3,7,5]
print ("list is-",list1)
print ("Reversing list")
for i in range(4,-1,-1):
    print (list1[i])
sum1=0
for i in list1 :
    sum1=sum1+i
print("sum of digit:",sum1)
