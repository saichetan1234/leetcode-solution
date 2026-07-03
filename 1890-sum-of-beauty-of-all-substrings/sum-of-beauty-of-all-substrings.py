class Solution:
    def beautySum(self, s: str) -> int:
        ans = 0

        for i in range(len(s)):
            temp = {}
            for j in range(i,len(s)):
                temp[s[j]] = temp.get(s[j],0) + 1
                beauty = max(temp.values())-min(temp.values())
                ans = ans + beauty
        return ans