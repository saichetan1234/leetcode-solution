class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int: 

        nums.sort()
        count  = 0
        left = 0
        right  = len(nums)-1
        mod = 10**9+7

        while(left<=right):
            if nums[left] + nums[right]<=target:
                count = count + pow(2,right-left,mod)
                left = left +1 
                pass
            else:
                right = right - 1 
        return count % mod     
       
        
        


     
     



         
        