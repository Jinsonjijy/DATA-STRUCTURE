def factorial(n):
    if n==1:
        return 1
    res=n*factorial(n-1)
    return res
n=int(input("enter the number:"))
print(factorial(n))
