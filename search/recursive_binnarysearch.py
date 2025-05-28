def binnarysearch(a,low,high,x):
    if low<=high:
        mid=low+(high-low)//2
        if a[mid]==x:
            return mid
        elif a[mid]<x:
            return binnarysearch(a,mid+1,high,x)
        else:
            return binnarysearch(a,low,mid-1,x)
    return False
arr=[23,24,12,15,27,89,100]
arr.sort()
b=binnarysearch(arr,0,len(arr)-1,15)
print(b+1)