"""this is mainly for usetig the bit

it is basically of a flaging or clearing a bit withot changing anyother bits


"""
def unset(n,pos):
    n&=~(1<<pos)
    return n
print(unset(15,1))