def perm_backtracK(nums):
    result=[]
    def backtrack(startindex):
        if startindex==len(nums):
            result.append(list(nums))
            return
        for i in range(startindex,len(nums)):
            nums[startindex],nums[i]=nums[i],nums[startindex]#this just change the values
            backtrack(startindex+1)#this create the permutation
            nums[startindex],nums[i]=nums[i],nums[startindex]#this undo that



    backtrack(0)
    return result
s={1,2,3}
permutation=perm_backtracK(list(s))
for p in permutation:
    print(tuple(p))