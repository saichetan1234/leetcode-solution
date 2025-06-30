class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums.sort()
        print(nums)
        j = 0
        maxi = 0
        

        for i in range(len(nums)):
            while(nums[i] - nums[j]>1):
                j = j +1
                print(j)
            if nums[i] - nums[j] ==1:
                maxi = max(maxi,i-j+1)
                
        
        
        return maxi
        
        