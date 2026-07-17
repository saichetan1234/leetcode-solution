class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        l = max(weights)
        h = sum(weights)
        ans = 0

        while(l<=h):
            mid = (l+h)//2
            days_took = 1
            loads = 0
            for i in range(0,len(weights)):
                if loads + weights[i]>mid:
                    days_took = days_took+1
                    loads = weights[i]
                else:
                    loads = loads + weights[i]
            
            if days_took<=days:
                ans = mid
                h = mid-1
            else:
                l = mid + 1
        return ans


