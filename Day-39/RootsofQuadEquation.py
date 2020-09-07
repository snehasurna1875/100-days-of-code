#Write  a program to solve quadratic equation

a=float(input("enter the value of cofficient of x^2\n"))
b=float(input("enter the value of cofficient of x\n"))
c=float(input("enter the value of constant\n"))
D=((b**2)-(4*a*c))**(0.5)
r1=(-b+D)/(2*a)
r2=(-b-D)/(2*a)


print("The roots of quadratic equation",r1,r2)                         
