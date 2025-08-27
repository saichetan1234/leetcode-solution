class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        if n==1:
            return 1
        odd=n**2
        even=n*(n+1)
        ans=0

        while even!=0:
            odd,even = even,odd%even
        return odd
        
        