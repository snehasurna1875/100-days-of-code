#WAP to take 5 values from user and insert the values in an array

import array as arr 
arr=arr.array('i',[])
for i in range(0,5):
    n=eval(input("enter the number-"))
    arr.append(n)
for i in range(0,5):
    print(arr[i],end=" ")
