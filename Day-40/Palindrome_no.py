#Wap to accept number from users and check whether its palindrome
a=eval(input("enter the no\n"))
s=a
result=0
while a > 0:
 num = a % 10
 result=result*10+num
 a = int(a/10)
if(s==result):
 print ("palindrome no")
else :
 print("not a palindrome no")