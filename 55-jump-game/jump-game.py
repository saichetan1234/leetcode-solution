class Solution:
    def canJump(self, nums: List[int]) -> bool:

        target = len(nums) -1

        for i in range(len(nums)-1,-1,-1):
            if i + nums[i]>=target:
                target = i
        
        if target ==0:
            return True
        else:
            return False
            

        