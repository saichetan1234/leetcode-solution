class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums = sorted(nums)

        left  = 0
        right = len(nums)-1
        b = []
        
        

        while left < right:
            sumi =nums[left] + nums[right] 

            if(sumi == target):
                return [left +1 , right + 1]


                
                
            if(sumi < target):
                left = left + 1
            else:
                right = right -1 
        return b
                
        