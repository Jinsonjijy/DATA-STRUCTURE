"""in the samedirection two pointer it is more like a sliding window i can express like this tow pointer that are moving in the same direction
taking sum and checking the sum if the sum of subarray is present then passing that subarray in this
initialize the left pointer as 0 and use a for loop to itrate form each element check if the target occur return the subba arayy


"""
def subinarr(arr,target):
    l=0
    total=0
    for r in range(len(arr)):
        total+=arr[r]
        while total>target:
            total-=arr[l]
            l+=1
        if target==total:
            return arr[l:r+1]
    return []
arr=[1,3,4,7,8,9,2]
target=8
print("the subarray"+str(subinarr(arr,target)))
