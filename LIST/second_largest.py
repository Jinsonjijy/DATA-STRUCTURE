arr=[1,5,6,8,3,2]
largest=float("-inf")
second=float("-inf")
for n in arr:
    if n > largest:
        second=largest
        largest=n
    elif n > second and n!=largest:
        second=n
print("second largest:"+str(second))