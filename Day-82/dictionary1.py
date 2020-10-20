'''WAP to accept both key and values from a user and create a dictionary with following constraints
1)The keys should not be numeric
2)The length of key should not be more than 6 and the value should only be even
'''
dictionary1={}
n=int(input("Enter the no of elements you want to enter-"))
for i in range(0,n):
    key=input("enter the string-")
    value=input("enter the value-")
    if key.isdigit() :
        print("key vaue is not string")
    else :
        if (len(key)<=6):
            if value.isdigit() :
                value=int(value)
                if value%2==0 :
                  dictionary1[key]=value
                else :
                  print ("value is not even")
            else :
                print ("value is not a number")
        else :
            
            print("key is more than 6")
print(dictionary1)
