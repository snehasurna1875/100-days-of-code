#WAP to accept 2 numbers from a user and display the sum of even and odd numbers

a = int(input("enter lower range-"))
b = int(input("Enter upper range-"))
evensum=0
oddsum=0
for i in range(a+1,b):
    if i%2==0 :
        evensum=evensum+i
    else :
        oddsum=oddsum+i
print ("Sum of even numbers-",evensum)
print ("Sum of odd numbers-",oddsum)
