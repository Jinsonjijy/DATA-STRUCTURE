"""
in this we are trying to make the anagrams with the help of backtracking
first we need a function we pass the word then inside that their is another function
"""
from collections import  Counter




def permutation_maker(word):
    res=[]
    count=Counter(word)
    def backtracking(current_path):
        if current_path:
            res.append("".join(current_path))
        if len(current_path)==len(word):
            return
        for char in sorted(count.keys()):
            if count[char]>0:
                current_path.append(char)
                count[char]-=1
                backtracking(current_path)
                count[char]+=1
                current_path.pop()
    backtracking([])
    return res


word=input("enter the word i will give you anagram for that😁:")
res=permutation_maker(word)
res.sort()
print(res)