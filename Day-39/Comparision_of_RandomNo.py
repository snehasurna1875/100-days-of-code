#Write a program to  generate 3 numbers and 2 check ifthey’re same.All same ->1st prize , 2 same -> 2nd prize , No same -> Try again


import random

a=eval(input("enter the first number of range-"))
b=eval(input("enter the last number of range -"))
c=random.randint(a,b)
d=random.randint(a,b)
e=random.randint(a,b)
if(c==d and d==e):
   print("1st Prize")
elif(c==d or d==e or c==e):
   print("2nd Prize")
else:
   print("Try Again")

