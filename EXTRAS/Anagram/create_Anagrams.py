from collections import Counter
def creating_anagrams(words):
    char_counts=Counter(words)
    result=[]
    def backtracking(current_path):
        if len(current_path)==len(words):
            result.append("".join(current_path))
            return
        #above one is the base case
        for char in sorted(char_counts.keys()):
            if char_counts[char]>0:
                current_path.append(char)
                char_counts[char] -=1
                backtracking(current_path)
                char_counts[char]+=1
                current_path.pop()
    backtracking([])
    return result
print(creating_anagrams(input("enter word")),end=" ")