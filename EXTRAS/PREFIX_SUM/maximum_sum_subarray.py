import math


def maximum_subarray(arr):
    n=len(arr)
    prefix_array=[0]*len(arr)
    prefix_array[0]=arr[0]
    min_prefix=0
    res=-math.inf
    for i in range(1,len(arr)):
        prefix_array[i]=prefix_array[i-1]+arr[i]
    for i in range(n):
        res=max(res,prefix_array[i]-min_prefix)
        min_prefix=min(min_prefix,prefix_array[i])
    return res


arr=[-1,6,4,-5,2,-4,3]
print(maximum_subarray(arr))
monke