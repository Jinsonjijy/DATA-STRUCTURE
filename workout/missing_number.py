arr=[1,2,2]
max_value=max(arr)
new=[0]*(max_value+2)
for num in arr:
    new[num]+=1
for i in range(1,len(new)):

    if new[i]==2:
        if new[i-1] ==0:
            print(i-1)
        elif new[i+1]==0:
            print(i+1)