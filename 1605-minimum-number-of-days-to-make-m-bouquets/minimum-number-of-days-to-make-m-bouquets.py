class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        
        n = len(bloomDay)

        if m*k > n:
            return -1 

        l=min(bloomDay)
        h = max(bloomDay)

        c = 0
        ans = 0
        

        

        while (l<=h):
            mid  = (l + h)//2
            c = 0
            num_of_b = 0           

            for i in bloomDay:
                if mid>=i:
                    c = c + 1
                else:
                    num_of_b = num_of_b + (c//k)
                    c = 0
            num_of_b = num_of_b + (c//k)
            
            if num_of_b>=m:
                ans = mid 
                h = mid -1
            else:
                l = mid + 1
        return ans
        