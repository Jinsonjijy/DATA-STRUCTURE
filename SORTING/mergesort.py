""" This is a type of sort in which
we implement divide and conquer m
means we divide the array into sub arrays and sort that sub arrays
then joint that sub arrays and sort the joined subarrays that is how it work
in the divide and conquer method that is in the merge sort we implement it by using two methods

"""
def mergesort(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    left=arr[:mid]
    right=arr[mid:]
    sortedleft=mergesort(left)
    sortedright=mergesort(right)
    return merge(sortedleft,sortedright)
def merge(left,right):
    result=[]
    i=j=0
    while i<len(left) and j< len(right):
        if left[i]<right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


n=int(input("enter the number of elements in the array:"))
myarray=[]
for i in range (n):
    myarray.append(int(input("enter the element")))
arr=mergesort(myarray)
print("sorted array"+str(arr))
