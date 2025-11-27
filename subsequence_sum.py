def subsequence(arr,target):
    res=[]
    target=target

    def backtracking(i,v,arr,n):
        if i>=n:
            if sum(v)==target:
                res.append(v[:])

            return
        v.append(arr[i])
        backtracking(i+1,v,arr,n)
        v.pop()
        backtracking(i+1,v,arr,n)
    backtracking(0,[],arr,len(arr))
    return res
arr=[4,5,9]
print(subsequence(arr,9))
