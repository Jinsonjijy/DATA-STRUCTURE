def max_subarray(arr):
    res=arr[0]
    max_end=arr[0]
    for i in range(1,len(arr)):
        max_end=max(max_end+arr[i],arr[i])# this is mainly for end if the end is -ve or something just change the max_end
        res=max(res,max_end)#for maximum sum
    return res
arr = [2, 3, -8, 7, -1, 2, 3]
print(max_subarray(arr))
