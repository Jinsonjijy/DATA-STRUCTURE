"""this is a code snippet for the insertions sort and
 it can implemented by the idea that
    an array that contain one part as sorted part and
        other conatiain unsorted path take the value from the unsroted(right)
            and append it to the correct position in the left sorted part array

"""
list1=[]

n=int(input("enter the number of elements:"))
for i in range (n):
    list1.append(input("enter the elements:"))
for i in range(1,n):#this loop will take the value we have to
    insert_index=i
    val=list1.pop(i)
    for j in range(i-1,-1,-1): #this loop is used to add the value to the sorted part and find the correct place to place the value
        if list1[j]>=val:
            insert_index=j
    list1.insert(insert_index,val)
print("the list:"+str(list1))

