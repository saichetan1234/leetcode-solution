class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        while(i<len(s)) and s[i]==" ":
            i = i + 1
        if i ==len(s):
            return 0

        
            
                
            
        sign = 1

        if s[i]=='-':
            sign = -1
            i = i + 1
        elif s[i]=='+':
            
            i = i+ 1
        
        ans = 0
        while i<len(s) and s[i].isdigit():
            ans = ans*10 + int(s[i])
            i = i+1
        ans = ans * sign
        

        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        if ans > INT_MAX:
            return INT_MAX
        if ans < INT_MIN:
            return INT_MIN

        return ans