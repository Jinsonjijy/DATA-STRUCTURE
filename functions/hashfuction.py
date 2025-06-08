"""have implemented the adding and searching in a hash map the searching in the hash map have a complexity of (1) so it is easy to implement
and it is easy to implement a hash map now we have to focus on how we can implement the 

"""
my_hash_set = [
    [None],
    ['Jones'],
    [None],
    ['Lisa'],
    [None],
    ['Bob'],
    [None],
    ['Siri'],
    ['Pete'],
    [None]
]

def hashfunction(value):
    sum_char=0
    for char in value:
        sum_char+=ord(char)
    return sum_char%10
# print("hash index"+str(hashfunction("bob")))
def contain(name):
    index=hashfunction(name)
    return my_hash_set[index]==name
def add(name):
    index=hashfunction(name)
    bucket=my_hash_set[index]
    if name not in bucket:
        bucket.append(name)
add(input("enter the name to add to the hashtable"))
print(my_hash_set)
print("pete"+str(contain("Jones")))