def check_set_unset(n,pos):
    return (n&(1<<pos))!=0
print(check_set_unset(32,5))
print(bin(32))