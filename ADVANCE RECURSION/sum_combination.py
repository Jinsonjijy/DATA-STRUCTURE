def printing_sum(arr,k):
    v=[]
    res=[]
    def backtracking(i,v,sum1,arr,n,k):
        if i>=n :
            if sum1==k:
                print(v)
                res.append(v.copy())
            return
        v.append(arr[i])
        sum1+=arr[i]
        backtracking(i+1,v,sum1,arr,n,k)
        v.pop()
        sum1-=arr[i]
        backtracking(i+1,v,sum1,arr,n,k)
    backtracking(0,[],0,arr,len(arr),k)
    return res
arr=[1,2,4,5,6,7]
k=9
print(printing_sum(arr,k))
