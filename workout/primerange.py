n=int(input("enter the number"))
count1=0
prime=[]

for i in range(2,n):
    flag=0
    for j in range(2,i):
        if i%j==0:
            flag=1
            break
    if flag==0:
        prime.append(i)
print(prime)
for i in range(len(prime)):
    for j in range(i+1,len(prime)):
        if (prime[i]+prime[j]) in prime:
            count1+=1

print(count1//2)

