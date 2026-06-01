class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def findfirst(nums,target):
            start = 0
            end = len(nums) -1
            first = len(nums)

            while(start<=end):
                mid = (start +end) //2

                if nums[mid] >=target:
                    first = mid
                    end = mid-1
                
                else:
                    start = mid + 1
            return first

        def findlast(nums,target):
            last_pos =len(nums)
            start = 0
            end = len(nums) -1

            while(start<=end):
                mid = start + (end-start)//2

                if nums[mid] > target:
                    last_pos=mid
                    end = mid -1 
                
                else:
                    start = mid + 1
            return last_pos
        ans = findfirst(nums,target)

        if ans == len(nums) or nums[ans]!=target:
            return [-1,-1]
        ans1 = findlast(nums,target) -1

        return [ans,ans1]
       
       


    