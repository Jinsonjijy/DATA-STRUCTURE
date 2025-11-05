""""this is an example of indirect recursion"""
def hello():
    print("hello i am hello")
    hai()

def hai():
    print("hai i am hai")
    hello()
hello()