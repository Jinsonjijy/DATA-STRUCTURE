def linnear(s,e):
    for i in range(len(s)):
        if e == s[i]:
            return True
    return False
a=linnear([2,3,4,5,6,7,34,54,12],12)
print(a)