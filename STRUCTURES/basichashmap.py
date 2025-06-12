"""
this is written by jisnon and i will not forgot that i done this
this is a basic implementation of hash map using the dictionary it is just a simple implementation
"""
# maps={}
# maps["canada"].append(["toronto","vancouver"])
# print(maps.values())
# basic implementation of dictionary because i forgot that
d={1:"jinson",2:"johan",3:"jissa",4:"jijy",5:"elsy"}
print(d.keys())
print(d.values())
print(d.items())
print(d[1])
print(d[3])
d.update({6: "hello"})
print(d)
d.update({int(input("enter the key")):input("enter the value")})
#in the dictionary the key cannot be duplicate or any copy cannot be done
print(d)
d={**d,"key2":"hello"}
#this is the unpacking operator used for combininng elements
print(d)
