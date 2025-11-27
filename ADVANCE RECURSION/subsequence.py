def subsequence(i,v,arr,n):
    if i>=n:
        print(v,end=",")
        return #dont forget to write return in the base case :
    v.append(arr[i])
    subsequence(i+1,v,arr,n)
    v.pop()
    subsequence(i+1,v,arr,n)
arr=[1,2,5]
subsequence(0,[],arr,len(arr))
print(arr)