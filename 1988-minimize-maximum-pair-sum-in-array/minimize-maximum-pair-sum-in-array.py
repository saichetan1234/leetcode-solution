class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        ans=float('-inf')
        l=0
        r=len(nums)-1

        while l<r:
            ans=max(ans,nums[r]+nums[l])
            l+=1
            r-=1
        return ans

        
        