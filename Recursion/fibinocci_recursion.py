import time
def fib(n):
    if n==0:
        return 0
    if n==1 or n==2:
        return 1
    else:
        return (fib(n-1)+fib(n-2))
start_time=time.time()

n=int(input("enter the range"))
print(fib(n))
end_time=time.time()
execution_time=start_time-end_time
print(f"The time taken{execution_time:.4f}")