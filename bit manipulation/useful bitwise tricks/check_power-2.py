def power_of_2(n):
    return n>0 and n&(n-1)==0 #here it return True only if the value greater than and and result will be 0
n=int(input("enter the number"))
print(power_of_2(n))