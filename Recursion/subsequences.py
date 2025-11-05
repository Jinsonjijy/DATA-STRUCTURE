def subsequence(i,v,arr,n):
    if i>=n:
        print(v,end=" ")
        return
    v.append(arr[i])
    subsequence(i+1,v,arr,n)
    v.pop()
    subsequence(i+1,v,arr,n)

arr=[]
n=int(input("enter the range:"))
print("enter the list elements:")
for i in range(n):
    arr.append(int(input()))
subsequence(0,[],arr,n)