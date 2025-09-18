""""fliping is mainly used for flip a certain bit only ulike using not just chnage 1 to 0 and 0 to 1 in number
that is how the flip is working
@@@@i can relate a scenario where set unset flip are used like oru mixer the mixer is our number

"""
def flip_bit(n,pos):

    n^=(1<<pos)
    return n
print(flip_bit(13,1))