"""
in this we are implementing the reccrussion by this we implemented it and understood it
for further info:https://www.geeksforgeeks.org/dsa/introduction-to-recursion-2/
"""
def sum_of_n(n):
    if n==1:
        return 1
    sum1=n+sum_of_n(n-1)
    return sum1
print(sum_of_n(5))
