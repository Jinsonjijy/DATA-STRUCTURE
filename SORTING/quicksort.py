"""
in this sort we are implementing an idea that we take a pivot element it may be the first element or the
last element or the median elemement and arrange the pivot in such a way that
the values less than pivot is placed in the left of the array while the value greater than the pivot
is placed in the right side of the pivot

"""


def partition(array,low,high):
    pivot=array[high]
    i=low-1# we use this i to place elements accoring to each place then we fix it
    for j in range(low,high):#in this j is just itrating from the low to high
        if array[j]<=pivot:
            i+=1 # i value is itrating to fix each value less the pivot
            array[i],array[j]=array[j],array[i]
    array[i+1],array[high]=array[high],array[i+1]#after that pivot element is placed in the i+1 position and replace the value with the i+1 element
    return i+1
def quicksort(array,low=0,high=None):
    if high is None:
        high=len(array)-1
    if low < high:
        pivot_index=partition(array,low,high)
        quicksort(array,low,pivot_index-1)
        quicksort(array,pivot_index+1,high)

n=int(input("enter the number of elements in the array:"))
myarray=[]
for i in range (n):
    myarray.append(int(input("enter the element")))
quicksort(myarray)
print("sorted array",myarray)