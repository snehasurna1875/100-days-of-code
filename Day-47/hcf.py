#WAP to find HCF of 2 numbers.

a = int(input("enter first number-"))
b = int(input("enter second number-"))

def hcfcalculate(x, y):
   while(y):
       x, y = y, x % y
   return x

hcf = hcfcalculate(a,b)
print("The HCF is", hcf)
