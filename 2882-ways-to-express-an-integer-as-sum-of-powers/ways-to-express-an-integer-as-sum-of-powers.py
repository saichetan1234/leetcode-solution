class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        arr=[]
        j=1
        while (j**x)<=n:
            arr.append(j**x)
            j+=1
        m=len(arr)
        dp=[[-1 for _ in range(n+1)] for _ in range(m)]
        def check(index,target):
            if target==0:
                return 1
            if index>=m or target<0:
                return 0
            if dp[index][target]!=-1:
                return dp[index][target]
            paths=0
            paths+=check(index+1,target)
            paths+=check(index+1,target-arr[index])
            dp[index][target]=paths
            return dp[index][target]
        return check(0,n) % (10**9+7)

        