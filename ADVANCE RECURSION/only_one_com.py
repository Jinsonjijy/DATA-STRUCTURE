def backtracking(i,v,arr,sum1,n,k):
    if i>=n:
        if sum1==k:
            print(v)
            return True
        return False
    v.append(arr[i])
    sum1+=arr[i]
    if (backtracking(i+1,v,arr,sum1,n,k)==True):
        return True
    v.pop()
    sum1-=arr[i]
    if(backtracking(i+1,v,arr,sum1,n,k)==True):
        return True
arr=[4,5,9]
k=9
print(backtracking(0,[],arr,0,len(arr),k))

