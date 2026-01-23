class Solution:
    def numberOfSubstrings(self, s: str) -> int:

        temp = {'a':0,'b':0,'c':0}

        l = 0
        count = 0

        for r in range(0,len(s)):
            temp[s[r]]+=1
            while temp['a'] > 0 and temp['b'] > 0 and temp['c']>0:
                count = count + len(s) - r 

                temp[s[l]]= temp[s[l]] - 1

                l = l+1
        return count
