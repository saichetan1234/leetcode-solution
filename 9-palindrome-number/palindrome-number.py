class Solution:
    def isPalindrome(self, x: int) -> bool:

        temp = x
        sum1 =0
        while(temp > 0):
            rem = temp %10
            sum1 =sum1 *10 +rem
            
            temp=temp//10

         

        if (sum1 == x):
            return True
         
        else:
            return False
        

        