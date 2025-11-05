def checking(first,second):
    if len(first)!=len(second):
        return False
    else:
        return sorted(first)==sorted(second)
first=input("enter the first word")
second=input("enter the second word")
print("checking the anagram",checking(first,second))