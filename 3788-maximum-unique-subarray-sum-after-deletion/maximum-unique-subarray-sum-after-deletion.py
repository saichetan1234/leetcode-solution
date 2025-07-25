class Solution:
    def maxSum(self, nums: List[int]) -> int:

        if max(nums)<=0:
            return max(nums)

        temp = {}

        for i in nums:
            temp[i] = temp.get(i,0) + 1
        b = []

        for key,value in temp.items():
            if key>0 :
                b.append(key)
        print(b)
        return sum(b)
        


        
        