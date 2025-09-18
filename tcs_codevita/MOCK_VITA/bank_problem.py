balance=int(input())
no_op=int(input())
msg=[]
done={}
commit={}
count=0
tnum=0
commit_no=0
for i in range(no_op):
    msg=[x for x in input().split()]
    if msg[0]=="read":
        print(balance)
    elif msg[0]=="credit":
        count+=1
        balance=balance+int(msg[1])
        done[count]=("credit",int(msg[1]))


    elif msg[0]=="debit":
        balance=balance-int(msg[1])
        count+=1
        done[count]=balance

        done[count]=("debit",int(msg[1]))
    elif msg[0]=="commit":
        commit_no+=1
        count=0
        commit[commit_no]=balance
        done.clear()


    elif msg[0]=="abort":
        if tnum in done:
            name,amt=done[tnum]

            if name=="credit":
                balance=balance-amt
            elif name=="debit":
                balance=balance+amt
            del done[tnum]




    elif msg[0]=="rollback":
        cnum=int(msg[1])
        if cnum in commit:
            balance=commit[cnum]
            done.clear()
print(balance)



