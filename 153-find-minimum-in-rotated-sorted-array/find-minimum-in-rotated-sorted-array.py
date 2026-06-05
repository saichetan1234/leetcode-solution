class Solution:
    def findMin(self, nums: List[int]) -> int:

        ans = float("inf")
        l = 0
        h = len(nums)-1

        while(l<=h):
            mid = (l+h)//2

            if nums[l]<=nums[mid]:
                ans = min(ans,nums[l])
                l = mid + 1
            else:
                ans = min(nums[mid],ans)
                h = mid -1
        return ans

        
       