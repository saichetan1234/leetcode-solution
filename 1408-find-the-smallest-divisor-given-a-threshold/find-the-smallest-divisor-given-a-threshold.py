import math
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:

        l = 1
        h  = max(nums)
        ans = []

        while(l<=h):
            mid = (l+h)//2
            ans1 = 0
            for i in nums:
                ans1 = ans1+ math.ceil(i/mid)
            if ans1<=threshold:
                ans .append(mid)
                
                h  = mid-1
            else:
                l= mid + 1

        return ans[-1]


        