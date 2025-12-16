class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        c = 1
        ans = 1

        for i in range(1,len(prices)):
            if prices[i] == prices[i-1] - 1:
                c = c+ 1
            else:
                c = 1
            ans = ans + c
        return ans

       

        