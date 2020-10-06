'''WAP  to accept a value from user and serach that  value in the array and if the value is present then check whether that value is even or odd'''
import array

arr1 = array.array('i', [1, 2, 3])

n=eval(input("enter the value to be searched-"))

for i in range(len(arr1)):
    if n==arr1[i]:
      if n%2==0 :
          print ("even")
      else:
          print ("odd")
   
