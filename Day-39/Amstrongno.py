#Write a program to check whether the no is Armstrong or not

a=eval(input("enter the  no\n"))
s=a
result=0
while a > 0:
    num = a % 10
    result = result + num**(3)
    a = int(a/10)

if(s==result):
   print(s,"is amstrong no")
else:
    print(s,"is not a amstrong no")

