class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        temp = {}
        b = []
        for i in nums:
            temp[i] = temp.get(i,0) + 1

        for key,value in temp.items():
            if value == 1:
                b.append(key)
        return b[0]