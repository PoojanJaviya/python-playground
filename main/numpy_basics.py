import numpy as np


#Creating Array
ls = [1,2,3,4,5,6,7,8,9,10]
arr = np.array(ls)

print(arr)

ls1 = [1,2,3]
ls2 = [4,5,6]

arr2d = np.array([ls1,ls2])
print(arr2d)


#Array Oprations
arr = np.array([1,2,3,4,5])
print(f"Array = {arr}")

print(f"Sum : {arr.sum()}")
print(f"Mean : {arr.mean()}")
print(f"Max : {arr.max()}")
print(f"Min : {arr.min()}")


mul = arr*2
square = arr**2

print(f"arr * 2 = {mul}")
print(f"arr square = {square}")


#Random & Reshape
arr = np.random.randint(1,20,12)

print(arr)

arr2 = arr.reshape(3,4)

print(arr2)

arr3 = arr.reshape(1,12)

print(arr3)



#Indexing & Slicing
arr = np.array([1,2,3,4,5])

print(arr[0])
print(arr[:3])
print(arr[3:])

arr2d = np.array([[1,2,3],
                  [4,5,6],
                  [7,8,9]])

print(arr2d[0])
print(arr2d[:,2])
print(arr2d[0,2])



#Mini Challenge
arr = np.random.randint(0,9,(5,5))

print(arr)

for i in range(len(arr)):
    print(f"Sum of row {i} = {np.sum(arr[i,:])}")
    print(f"Sum of column {i} = {np.sum(arr[:,i])}")
for i in range(len(arr)):
    print(f"Max of row {i} = {np.max(arr[i,:])}")
    print(f"Min of column {i} = {np.min(arr[:,i])}")

