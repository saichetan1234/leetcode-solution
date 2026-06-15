class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l  = max(nums)
        h = sum(nums)
        ans = 0

        while(l<=h):
            mid = (l+h)//2
            sumi = 0
            partition = 1

            for i in range(0,len(nums)):
                if sumi + nums[i]>mid:
                    partition+=1
                    sumi = nums[i]

                else:

                    sumi = sumi + nums[i]
            if partition<=k:
                ans = mid
                h = mid -1
            else:
                l= mid + 1
        return ans


        