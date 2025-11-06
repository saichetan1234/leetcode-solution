class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.

        """
        
        b = []
        l = 0
        r = 0
        j = 0

        while l<m and r<n:
            if nums1[l]>nums2[r]:
                b.append(nums2[r])
                r = r + 1
                
            else:
                b.append(nums1[l])
                l = l + 1
                
        
        while r <n:
            b.append(nums2[r])
            r = r + 1
        
        while l < m:
            b.append(nums1[l])
            l = l + 1
        print(b)


        for i in range(len(b)):
            nums1[i] = b [i]
        return nums1


        