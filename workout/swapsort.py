import ast

arr = [15,19,26,30,5,11]
arr1=[]
swap=0
for i in range(len(arr)):
    arr1.append([arr[i],i])

arr2=sorted(arr1)
print(arr2)
for i in range(len(arr1)):
    if arr2[i][1]<arr1[i][1]:
        swap+=1
    else:
        continue
print(swap)