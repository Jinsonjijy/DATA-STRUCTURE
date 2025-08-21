def twosum(arr,target):
    l = 0
    curr_sum = 0
    r = len(arr) - 1
    while l < r:
        curr_sum = arr[l] + arr[r]
        if curr_sum == target:
            return [l,r]
        elif curr_sum > target:
            r -= 1
        else:
            l += 1
    return []
arr=[1,2,4,7,3,5,6]
arr.sort()
target=9
print("index :"+str(twosum(arr,target)))
""" the thing we want to do is we want fo find the sum "target" """

