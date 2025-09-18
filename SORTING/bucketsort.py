def bucketsort(arr):
    n=len(arr)
    max_value=max(arr)
    bucket_size=(max_value//n)+1

    bucket=[[] for i in range(n)]
    for num in arr:
        ind=num//bucket_size
        bucket[ind].append(num)
    for buc in bucket:
        buc.sort()#  also you can implement it with other sorting algorithm but i just used in-built sort function
    index=0
    for buc in bucket:
        for val in buc:
            arr[index]=val
            index+=1


arr=[]
n=int(input("enter the number of element"))
for i in range(n):
    arr.append(int(input()))
bucketsort(arr)
print("the sorted array:",arr)