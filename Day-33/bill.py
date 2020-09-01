
'''Calculate the telephone bill
For fisr 100 call its free
for 101-200 call 1 rupee charge
for 201-300 call 2 rupees charge
For 301-400 call 3 rupees charge
greater than 401 5 rupees charge'''




'''code'''

n=eval(input("Enter the no of call"))
s=0
sum1=sum2=sum3=sum4=0
if n<=100 :
   print ("Free")
if 100<n<201:
   s=n-100
   sum1=s*1
if 200<n<301:
   s=n-200
   sum2=s*2

if 300<n<401:
   s=n-300
   sum3=s*3
if n>400:
   s=n-400
   sum4=s*5

print (sum1+sum2+sum3+sum4)
      
      
      
