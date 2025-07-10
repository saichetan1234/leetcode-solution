class Solution:
    def myPow(self, x: float, n: int) -> float:

        if n < 0:
            x = 1 / x
            n = -n
        
        ans  = 1

        while n :
            if n%2 == 1:
                ans  = ans * x
            x = x * x
            n = n//2
        return ans

        
        