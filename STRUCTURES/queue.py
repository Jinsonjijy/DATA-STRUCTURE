print("1 for insertion 2 for deletion 3 for display")

queue=[]
while True:
    ch = int(input("enter the choice:"))
    if ch==1:
        n=int(input("enter the number"))
        queue.append(n)
    elif ch==2:
        queue.pop(0)
    elif ch==3:
        for i in range (len(queue)):
            print(queue[i],end="\t")
    else:
        break