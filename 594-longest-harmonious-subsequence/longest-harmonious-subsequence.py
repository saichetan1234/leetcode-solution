class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums.sort()
        m = []

        for i in range(len(nums)-1):
            if abs(nums[i] - nums[i+1]) == 1:
                m.append([nums[i],nums[i+1]])
        k = Counter(nums)
        maxi = 0
        for i,j in m:
            maxi = max(maxi,k[i]+k[j])
        return maxi




       

        
        