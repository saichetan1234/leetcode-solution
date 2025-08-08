class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxi = 0
        ans = prices[0]

        for i in prices[1:]:
            if i > ans:
                maxi = max(maxi,i-ans)
            else:
                ans = i
        return maxi

        
        

       
       
       
       
        
        