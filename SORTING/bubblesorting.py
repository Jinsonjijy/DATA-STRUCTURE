n=int(input("enter the number of elements:"))
list1=[]
for i in range (n):
    list1.append(int(input("enter the data:")))
swap=False
while not swap: #this loop is used to pass the inner loop (it is mainly used to 1 pass 2 pass 3 pass for that we use this loop)
    swap=True
    for i in range (1,n): # this is the loop that do the comparison
        if list1[i-1]>list1[i]:
            swap=False
            list1[i],list1[i-1]=list1[i-1],list1[i]

for i in range(n):
    print(list1[i],end="\t")