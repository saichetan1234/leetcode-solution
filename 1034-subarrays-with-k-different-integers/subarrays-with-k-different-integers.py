class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def ans(nums,k):


            temp  = {}
            l = 0
            count = 0

            for r in range(0,len(nums)):
                temp[nums[r]] = temp.get(nums[r],0) +1
                while len(temp) > k:
                    temp[nums[l]] -=1
                    if temp[nums[l]] ==0:
                        del temp[nums[l]]
                    l = l + 1

                count  = count + r-l+1
            return count
        return ans(nums,k) - ans(nums,k-1)
            