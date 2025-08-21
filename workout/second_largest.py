def second_largest(arr):
    first = float("-inf")
    second = float("-inf")
    for num in arr:
        if first < num:
            second = first
            first = num
        elif first > num > second:
            second = num
    return str(second)

n=int(input("enter the number of elements"))
arr=[]

for i in range(n):
    arr.append(int(input()))
print("the second largest element:"+second_largest(arr))
