n=int(input("enter the number of elements:"))
list1=[]
for i in range (n):
    list1.append(int(input("enter the data:")))
swap=False
for j in range (n): #this loop is used to pass the inner loop (it is mainly used to 1 pass 2 pass 3 pass for that we use this loop)

    for i in range (1,n-j-1): # this is the loop that do the comparison
        if list1[i-1]>list1[i]:
        
            list1[i],list1[i-1]=list1[i-1],list1[i]

for i in range(n):
    print(list1[i],end="\t")