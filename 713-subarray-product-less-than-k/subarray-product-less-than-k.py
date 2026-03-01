class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:

        if k <=1:
            return 0
        product  =  1

        count  = 0
        b = []
        l = 0

        for i in range(len(nums)):
            product = product * nums[i]

            while product>=k:
                product = product //nums[l]
                
                
                l = l + 1
            count  = count + (i-l+1)

        return count

        