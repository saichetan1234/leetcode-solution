class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:

        l= 1
        n = len(nums)

        h = len(nums)-2
        if n ==1:
            return nums[n-1]

        if nums[1]!=nums[0]:
            return nums[0]
        if nums[n-1]!=nums[n-2]:
            return nums[n-1]

        while(l<=h):
            mid  = (l+h)//2

            if nums[mid]!=nums[mid-1] and nums[mid]!=nums[mid+1]:
                return nums[mid]

            if mid%2!=0 and nums[mid-1]==nums[mid] or mid %2 == 0 and nums[mid] == nums[mid +1]:
                l = mid + 1
            else:
                h = mid -1
        return -1

       
        