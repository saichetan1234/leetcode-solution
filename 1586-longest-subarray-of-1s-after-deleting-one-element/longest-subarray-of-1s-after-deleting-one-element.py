class Solution:
    def longestSubarray(self, nums: List[int]) -> int:

        k = 1
        maxi = 0
        one_freq = 0
        l = 0

        for r in range(len(nums)):
            if nums[r] == 1:
                one_freq +=1
                
            while (r-l+1) - one_freq >k:
                if nums[l] == 1:
                    one_freq-=1
                l = l + 1
            maxi = max(maxi,r-l+1)
        return maxi - 1
                