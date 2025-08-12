class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        arr=[]
        j=1
        while (j**x)<=n:
            arr.append(j**x)
            j+=1
        m=len(arr)
        dp=[[0 for _ in range(n+1)] for _ in range(m+1)]
        dp[0][0]=1
        for i in range(1,m+1):
             for j in range(n+1):
                 dp[i][j]=dp[i-1][j]
                 if i**x<=j:
                     dp[i][j]+=dp[i-1][j-i**x]
        return dp[m][n] % (10**9+7)
        

        
        