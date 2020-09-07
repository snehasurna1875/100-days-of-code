#Write a Program to calculate area of a triangle(if a,b,c are three sides then calculate S and A)

a=float(input("enter the first side\n"))
b=float(input("enter the second side\n"))
c=float(input("enter the third side\n"))
s=(a+b+c)/2
print("The value of s",s)
A=(s*(s-a)*(s-b)*(s-c))**(0.5)
print("The area of triangle",A)

