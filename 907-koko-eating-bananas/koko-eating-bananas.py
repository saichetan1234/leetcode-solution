import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l = 1
        hi = max(piles)
        ans = float('inf')
        

        while(l<=hi):
            mid = (l+hi)//2
            ans1 = 0

            for i in piles:
                ans1 = ans1+math.ceil(i/mid)
            
            if ans1<=h:
                ans = min(ans,mid)
                hi = mid -1
            else:
                l = mid + 1
        return ans
            






       
       