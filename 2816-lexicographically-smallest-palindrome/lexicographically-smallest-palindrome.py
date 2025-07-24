class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        b = list(s)

        l = 0
        r = len(s) -1

        while(l<r):
            if b[l]!=b[r]:
                maxi = min(b[l],b[r])
                b[l] = maxi
                b[r] = maxi

            l = l+ 1
            r = r -1  
        print(b)
        return "".join(b)    
        