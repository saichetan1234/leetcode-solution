class Solution:
    def minimumSwaps(self, nums: list[int]) -> int:

        swaps = 0
        
        zeros = nums.count(0)


        n = len(nums) - zeros

        for i in range(0,n):
            if nums[i] == 0:
                swaps  = swaps + 1
        return swaps

        