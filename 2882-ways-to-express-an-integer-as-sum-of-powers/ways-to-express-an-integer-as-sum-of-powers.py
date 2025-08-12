class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        arr=[]
        j=1
        while (j**x)<=n:
            arr.append(j**x)
            j+=1
        m=len(arr)
        base=n+1
        dp={}
        def check(index,target):
            if target==0:
                return 1
            if index>=m or target<0:
                return 0
            key=index*base+target
            if key in dp:
                return dp[key]
            paths=0
            paths+=check(index+1,target)
            paths+=check(index+1,target-arr[index])
            dp[key]=paths
            return dp[key]
        return check(0,n) % (10**9+7)

        