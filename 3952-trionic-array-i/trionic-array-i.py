class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        temp1 = [nums[0]]
      
        c = 0

        for i in range(1,len(nums)):
            if nums[i-1]< nums[i]:
                temp1.append(nums[i])
            else:
                break
           
        print(temp1)

        temp2 = [nums[len(temp1)-1]]

        for i in range(len(temp1),len(nums)):
            if nums[i-1] > nums[i]:
                temp2.append(nums[i])
            else:
                break
        print(temp2)

        ans = len(temp1)+len(temp2) -2

       
       
       
       
        temp3 = [nums[ans]]

        for i in range(ans,len(nums)):
            c = c + 1
        print(c)

        for i in range(ans+1 ,len(nums)):
            if nums[i-1] < nums[i]:
                temp3.append(nums[i])
           

        print(temp3)

        if c != len(temp3):
            return False


        if len(temp1) > 1 and len(temp2) > 1 and len(temp3) > 1:
            return True
        else:
            return False


      
        

        

        