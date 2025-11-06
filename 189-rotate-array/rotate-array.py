class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.

        """
        b = []
        c = []
        k = k % len(nums)

        for i in range(len(nums) - k,len(nums)):
            b.append(nums[i])
        print(b)

        for i in range(0,len(nums) - k):
            c.append(nums[i])
        print(c)

        d =  b + c
        print(d)

        for i in range(len(nums)):
            nums[i] = d[i]
        
        print(nums[i])




        