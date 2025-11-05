def factorial(n):
    if n==1:
        return 1
    #so basically this is the base case where the condition checks and then return 
    res=n*factorial(n-1)
    return res
n=int(input("enter the number:"))
print(factorial(n))
