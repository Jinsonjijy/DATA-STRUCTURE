def binnary(a,low,high,x):
    """here in this functiion were are planning to implement the binnary search in the itrative manner this is done for better understadnding of the data structure and algorithms"""
    while low<=high:
        mid=low+(high-low)//2
        if a[mid]==x:
            return mid
        elif a[mid]<x:
            low=mid+1
        else:
            high=mid-1
    return False
arr=[23,45,41,47,67,89,100]
a=binnary(arr.sort(),0,len(arr)-1,100)
print(a)