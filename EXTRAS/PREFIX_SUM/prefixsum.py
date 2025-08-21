n=int(input("enter the number"))
arr=[]
for i in range(n):
    arr.append(int(input()))
prefixSum = [0] * n

    # initialize the first element
prefixSum[0] = arr[0]

# Adding present element with previous element
for i in range(1, n):
    prefixSum[i] = prefixSum[i - 1] + arr[i]
print(prefixSum)