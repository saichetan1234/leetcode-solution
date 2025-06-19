class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        
        nums.sort()
        arr=[]

        for i in range(len(nums)):
            if len(arr)==0 or nums[i]-arr[-1]>k:
                arr.append(nums[i])
        return len(arr)