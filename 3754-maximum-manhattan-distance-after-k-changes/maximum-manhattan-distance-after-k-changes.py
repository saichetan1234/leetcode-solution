class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        ans=0
        n = 0
        so = 0
        w = 0
        e = 0

        for i in range(len(s)):
            if s[i] == 'N':
                n = n+1
            elif s[i] == 'E':
                e = e+1
            elif s[i] == 'S':
                so = so+1
            elif s[i] == 'W':
                w = w+1

            dis = abs(so-n) + abs(w-e)
            ans = max(ans,min(dis+2*k,i+1))
        return ans



        
