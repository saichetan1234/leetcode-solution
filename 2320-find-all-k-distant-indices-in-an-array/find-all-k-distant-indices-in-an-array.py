from typing import List

class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
       
        b = []
        c = []

        for i in range(0,len(nums)):
            if nums[i] == key:
                b.append(i)
        print(b)
        
        for i in range(0,len(nums)):
            for j in b:
                if abs(i-j)<=k:
                    c.append(i)
                    break
        return c

        