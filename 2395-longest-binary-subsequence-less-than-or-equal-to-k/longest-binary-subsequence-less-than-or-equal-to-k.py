class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:

        temp = s[::-1]
        count = 0
        rem = 0
        index = len(s)


        for i in range(len(temp)):
            power  = int(temp[i]) * pow(2,i)
            if count + power <=k:
                count = count + power
            else:
                index = i
                break
        for j in range(index,len(s)):
            if temp[j]=='1':
                rem = rem +1
        return len(s) - rem
                



        
        