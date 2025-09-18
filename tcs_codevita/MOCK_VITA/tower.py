arr=[4,8,3,5,7]
min_value=float("inf")
min_value2=float("inf")
res=[]
for i in range(len(arr)-1):
    min_value = float("inf")
    l=i-1
    r=i+1
    while l>=0 or r<=len(arr):
        min_value=min(min_value,arr[l],arr[r])
        l-=1
        r+=1
    if min_value<arr[i]:
        res.append(arr.find(min_value))


