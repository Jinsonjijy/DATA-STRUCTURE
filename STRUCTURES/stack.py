print("1 for insertion 2 for deletion 3 for display")

stack=[]
while True:
    ch = int(input("enter the choice:"))
    if ch==1:
        n=int(input("enter the number"))
        stack.append(n)
    elif ch==2:
        stack.pop()
    elif ch==3:
        for i in range (len(stack)):
            print(stack[i],end="\t")
    else:
        break