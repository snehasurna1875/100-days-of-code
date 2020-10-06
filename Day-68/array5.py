#WAP to get the number of occurence of a specifiecd element in the array
import array

arr1 = array.array('i', [1, 2, 2, 4, 3, 3])
print("array")
print()
for i in range(len(arr1)):
    print(arr1[i],end="")
print()
n=eval(input("enter the number-"))
print("Occurence of number",arr1.count(n))
