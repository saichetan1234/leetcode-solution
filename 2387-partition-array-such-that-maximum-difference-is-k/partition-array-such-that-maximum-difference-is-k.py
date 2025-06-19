class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        
        nums.sort()
        count = 1
        ans = nums[0]

        for i in range(1,len(nums)):
            if nums[i] - ans > k:
                count = count +1
                ans = nums[i]
        return count