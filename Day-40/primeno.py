#Wap and display prime numbers between that numbers
a = int(input("enter lower range-"))
b = int(input("Enter upper range-"))

for number in range(a,b + 1):
 if number > 1:
      for i in range(2,number):
         if (number % i) == 0:
             break
         else: 
            print(number)