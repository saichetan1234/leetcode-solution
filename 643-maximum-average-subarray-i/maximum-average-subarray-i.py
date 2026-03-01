class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        l = 0
        sumi = 0 

        b = []

        for r in range(0,len(nums)):
            sumi  =  sumi + nums[r]

            if r -l+1 ==k:
                b.append(sumi)
                sumi = sumi -nums[l]
                l = l + 1
        maxi = max(b)

        return maxi/k

        
        