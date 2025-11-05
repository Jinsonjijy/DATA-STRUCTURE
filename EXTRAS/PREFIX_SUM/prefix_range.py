"""in this we are implementing the prefix sum arry and getting the sum of a range elements with the help of prefix sum
the task is very easy
making the prefix:O(n)
getting the value:O(1)

"""




def prefix_sum(arr):

    prefix_arr=[0]*len(arr)
    prefix_arr[0]=arr[0]
    for i in range(1,len(arr)):
        prefix_arr[i]=prefix_arr[i-1]+arr[i]
    return prefix_arr
def range_getting(arr,low=None,high=None):
    return arr[high]-arr[low-1]


arr=[1,2,4,-2,1,7,8]
prefix_arr=prefix_sum(arr)
sum=range_getting(prefix_arr,2,5)
print(sum)

