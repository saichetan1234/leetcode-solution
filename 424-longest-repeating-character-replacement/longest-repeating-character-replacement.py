class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxi_freq = 0
        maxi = 0
        l = 0

        temp = {}

        for r in range(len(s)):
            temp[s[r]] = temp.get(s[r],0) + 1
            maxi_freq = max(maxi_freq,temp[s[r]])

            while(r-l+1) - maxi_freq > k:
                temp[s[l]]-=1
                l = l+1
            maxi = max(maxi,r-l+1)
        return maxi

        


        

        