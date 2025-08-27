class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        if n==1:
            return 1
        odd=n**2
        even=n*(n+1)
        ans=0
        for i in range(1,min(odd,even)):
            if odd%i==0 and even%i==0:
                ans=i
        return ans
        