def countinsort(arr):
    max_value=max(arr)
    count=[0]*(max_value+1)
    while len(arr)>0:
        num=arr.pop(0)
        count[num]+=1
    for i in range (len(count)):
        while count[i]>0:
            arr.append(i)
            count[i]-=1
    return arr
n=int(input("enter the number of elements in the array:"))
myarray=[]
for i in range (n):
    myarray.append(int(input("enter the element")))
countinsort(myarray)
print(myarray)