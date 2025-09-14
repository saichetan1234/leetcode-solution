class Solution:
    def maxKDistinct(self, nums: List[int], k: int) -> List[int]:

        x=list(set(nums))
        x.sort(reverse=True)
        return x[:k]
        