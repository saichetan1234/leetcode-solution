class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:

        b = []
        sumi  = 0

        count  = 0
        l =0
        b = []

        for i in range(len(nums)):
            sumi = sumi + nums[i]

            while sumi*(i-l+1) >= k:
                sumi =  sumi - nums[l]
                l = l + 1

            count  =  count +(i-l+1)

        return count 

        