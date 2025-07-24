class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        l=0
        r=len(s)-1
        s1=list(s)
        while l<r:
            if s1[l]!=s1[r]:
                if s1[l]<s1[r]:
                    s1[r]=s1[l]
                else:
                    s1[l]=s1[r]
            l+=1
            r-=1

        return "".join(s1)
        