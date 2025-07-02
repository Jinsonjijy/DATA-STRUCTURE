"""
in this sorting algorithm we take and non negative unsorted array and take the least signinficant digit and based
on that arranga in a bucket(where a bucket is a 2 dimensional list)
and then again add to the orginal list and then take next digit and then next digit and go on at last print the
original arary
the complexity:O(nk)

"""
n=int(input("enter the number of elements:"))
arr=[]
for i in range(n):
    arr.append(int(input("enter the element:")))
print(arr)
max_value=max(arr)
radixarray=[[],[],[],[],[],[],[],[],[],[]]
exp=1
while max_value//exp>0:# this is for itrating the maxvalue digits
    while len(arr)>0:
        val=arr.pop()
        radix_index=(val//exp)%10
        radixarray[radix_index].append(val)
    for bucket in radixarray:
        while len(bucket)>0:
            val=bucket.pop()
            arr.append(val)
    exp*=10
print("sorted array:"+str(arr))

