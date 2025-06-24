from typing import List

class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        key_indices = []
        result = []

      
        for i in range(len(nums)):
            if nums[i] == key:
                key_indices.append(i)

        
        for i in range(len(nums)):
            for j in key_indices:
                if abs(i - j) <= k:
                    result.append(i)
                    break   

        return result
