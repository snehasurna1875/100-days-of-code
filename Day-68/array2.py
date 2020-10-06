#WAP to delete a value at particular index
arr1 = array.array('i', [1, 2, 3])
for i in range(0,3):
    print(arr1[i],end=" ")
print()
n=eval(input("enter the index you want to delete-"))
arr1.pop(n)
for i in range(len(arr1)):
    print(arr1[i],end="")
