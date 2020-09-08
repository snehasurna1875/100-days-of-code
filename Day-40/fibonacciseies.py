#Wap to fetch two numbers from a user and display fibonacci series betweenthem

a = int(input("enter lower range-"))
n = int(input("Enter upper range-"))
b = 1
sum = a
count = 1
print("Fibonacci Series: ", end = " ")
while(count < n-1):
 print(sum, end = " ")
 count += 1
 a = b
 b = sum
 sum = a + b
