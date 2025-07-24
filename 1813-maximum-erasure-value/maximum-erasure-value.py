class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
       
        seen = set()
        maxi = 0
        curr = 0

        l = 0

        for i in range(0,len(nums)):
            while(nums[i] in seen):
                seen.remove(nums[l])
                curr = curr-nums[l]
                l = l + 1
            
            seen.add(nums[i])
            curr = curr + nums[i]
            maxi = max(curr,maxi)

        return maxi
            
            
            