#WAP to generate the output 1 12 123 1234 
n=int(input("Enter the number you want the pattern to be printing-\n"))
for i in range(1,n+2):
    for j in range(1,i):
        print (j,end=" ")
    print(" ")  

