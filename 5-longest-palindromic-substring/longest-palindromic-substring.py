class Solution:
    def longestPalindrome(self, s: str) -> str:

        res = 0
        string = ""

        for i in range(len(s)):
            l = i
            r = i

            while l>=0 and r<len(s) and s[l]==s[r]:
                if r-l+1>res:
                    string = s[l:r+1]
                    res = r-l+1
                l = l-1
                r = r+1
            l = i 
            r = i+1

            while l>=0 and r<len(s) and s[l]==s[r]:
                    if r-l+1>res:
                        string = s[l:r+1]
                        res = r-l+1
                    l = l-1
                    r = r+1
        return string


        
            


                   
                
            