class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b = [prices[0]]
        ans = 0

        for i in range(1,len(prices)):
            if prices[i]>prices[i-1]:
                ans = ans + prices[i] - prices[i-1]
        return ans
           
           