class Solution:
    def wordBreak(self, s: str, w: List[str]) -> bool:

        dp = [False]*(len(s)+1)

        dp[0] = True

        for i in range(1,len(s)+1):
            for j in range(i):
                if dp[j] and s[j:i] in w:
                    dp[i] = True
                    break
        return dp[-1]
       
       