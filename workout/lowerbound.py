def binnary_search(arr,target):
    l=0
    r=len(arr)-1
    ans=0
    while l<=r:
        mid=(l+r)//2
        if arr[mid]>=target:
            ans=mid
            #storing the mid value
            r=mid-1
        else:
            l=mid+1

    return ans


arr=[1,5,6,10,13]
target=5
print(binnary_search(arr,target))
