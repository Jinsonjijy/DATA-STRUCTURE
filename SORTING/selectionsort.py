"""

this sort implementation ideas
is that taking the smallest element in the array
 and moving it to the front of the array
 and itrating it n times that how it is performed


        """
list1=[]

n=int(input("enter the number of elements:"))
for i in range (n):
    list1.append(input("enter the elements:"))
for i in range(n-1):
    min_index=i
    for j in range(i+1,n):
        if list1[j]<list1[min_index]:
            min_index=j
    data=list1.pop(min_index)
    list1.insert(i,data)
for i in range (n):
    print(list1[i],end="  ")
