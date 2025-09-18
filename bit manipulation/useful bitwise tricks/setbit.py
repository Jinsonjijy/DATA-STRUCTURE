""" basically oning all the bits's in a  binnary number it is called setbit


*********Algorithms & Competitive Programming******

Used in problems involving subsets, masks, DP on bitmasks.
Setting a bit means: “include this element in the subset”.
"""
def setbit(n,pos):
    n|=(1<<pos)
    return n
print(setbit(5,1))