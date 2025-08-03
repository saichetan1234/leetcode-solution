class Solution:
    def longestSubarray(self, nums: List[int]) -> int:

        b= []
        maxi = max(nums)
        c = 0

        for i in nums:
            if i == maxi:
                c = c + 1
                b.append(c)
            else:
                c = 0
        return max(b)



        