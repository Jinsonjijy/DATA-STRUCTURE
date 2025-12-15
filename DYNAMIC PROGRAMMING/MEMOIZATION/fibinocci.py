def fibinocci(n):
    dp=[-1]*(n+1)
    def memo(n):
        if n==0:
            return 0
        if n==1:
            return 1
        if dp[n]!=-1: return dp[n]
        dp[n] = memo(n-1)+memo(n-2)
        return dp[n]
    return (memo(n))
print(fibinocci(7))