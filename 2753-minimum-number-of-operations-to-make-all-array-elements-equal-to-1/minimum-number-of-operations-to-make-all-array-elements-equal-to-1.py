import math
from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)

        # If any element is already 1, we need n - count(1) operations
        ones = nums.count(1)
        if ones > 0:
            return n - ones

        # If gcd of whole array is not 1, impossible
        total_gcd = 0
        for x in nums:
            total_gcd = math.gcd(total_gcd, x)
        if total_gcd != 1:
            return -1

        # Find the shortest subarray with gcd == 1
        min_len = float('inf')
        for i in range(n):
            g = nums[i]
            if g == 1:
                min_len = 1
                break
            for j in range(i + 1, n):
                g = math.gcd(g, nums[j])
                if g == 1:
                    min_len = min(min_len, j - i + 1)
                    break

        # min_len must exist (total_gcd == 1 guarantees that)
        return min_len + n - 2
