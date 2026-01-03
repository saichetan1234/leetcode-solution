class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        b=set(nums)
        c = []
        for i in range(1,len(nums)+1):
            if i not in b:
                c.append(i)
        print(c)
        print(b)
        print(len(nums))
        return c