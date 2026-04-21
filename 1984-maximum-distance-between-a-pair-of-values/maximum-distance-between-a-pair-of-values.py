class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:

        i = 0
        j = 0

        while i <len(nums1) and j<len(nums2):
            if nums1[i]>nums2[j]:
                i = i + 1
            j = j + 1
        
        return max(0,j-i-1)

        
          