#wap to reverse the order of the items in the array
import array

arr1 = array.array('i', [1, 2, 3])
print("array")
print()
for i in range(len(arr1)):
    print(arr1[i],end="")

arr1.reverse()
print()
print("after reversing")
for i in range(len(arr1)):
    print(arr1[i],end="")
