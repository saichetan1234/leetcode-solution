class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        maxi = 0
        l = 0
        zero = 0

        for r in range(0,len(nums)):
            if nums[r] == 0:
                zero = zero + 1
            while zero>k:
                if nums[l] == 0:
                    zero = zero-1
                l = l+1

            maxi = max(maxi,r-l+1)
        print(maxi)
        return maxi


            
            