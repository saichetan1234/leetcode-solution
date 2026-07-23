class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:

        if len(nums)<=2:
            return len(nums)
        
        bits = len(nums).bit_length()

        return 2 ** bits

        
        