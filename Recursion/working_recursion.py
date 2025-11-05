"""this program mainly deal with how the recursion work"""
def working(test):
    if test<1:
        return
    else:
        print(test,end="")
        working(test-1)
        print(test,end="")
        return
test=3
working(test)
