#WAP a python program to remove the first occurerence of a specified element from an array
import array

arr1 = array.array('i', [1, 2, 2, 4, 3, 3])
print("array")
print()
for i in range(len(arr1)):
    print(arr1[i],end="")
print()
n=eval(input("enter the number-"))
for i in range(len(arr1)):
    if n==arr1[i]:
        arr1.pop(i)
        break;
for i in range(len(arr1)):
    print(arr1[i],end="")
print()
