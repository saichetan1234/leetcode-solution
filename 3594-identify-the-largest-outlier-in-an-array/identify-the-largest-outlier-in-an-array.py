class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        count={}
        for i in range(len(nums)):
            count[nums[i]]=i
        
        sums=sum(nums)
        maxi=float('-inf')
        for i in range(len(nums)):
            x=sums-nums[i]
            if x/2 in count and count[x/2]!=i:
                maxi=max(maxi,nums[i])
        return maxi
        