from collections import Counter
def valid_anagrams(s,p):
    if len(p)>len(s):
        return []
    window_p=Counter(p)#created a window for the p to check the value it is fixed it wont change
    window_s=Counter(s[:len(p)])#this changes always right side insert new character while left side delete characters
    for i in range(len(p),len(s)):

        window_s[s[i]]=+1
        left_char=

