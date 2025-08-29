def max_subarray(arr):
    curr_sum=0
    res=0
    for i in range(len(arr)):
        curr_sum=0
        for j in range(i,len(arr)):
            curr_sum=curr_sum+arr[j]
            res=max(res,curr_sum)
    return res

arr = [2, 3, -8, 7, -1, 2, 3]
print(max_subarray(arr))