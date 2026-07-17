class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        l  = max(weights)
        h = sum(weights)

        ans  = 0

        while(l<=h):
            mid = (l+h)//2

            days_taking = 1
            loads = 0

            for i in range(len(weights)):

                if (loads+weights[i])>mid:
                    loads = weights[i]
                    days_taking = days_taking + 1
                else:
                    loads = loads+weights[i]
                
            
            if days_taking<=days:
                ans  = mid
                h = mid -1 
            else:
                l  =  mid + 1
        return ans

        
       