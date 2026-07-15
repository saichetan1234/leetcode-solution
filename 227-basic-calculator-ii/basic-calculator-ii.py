class Solution:
    def calculate(self, s: str) -> int:

        b = []
        sign = "+"
        rem  = 0

        for i in range(len(s)):
            if s[i].isdigit():
                rem = rem * 10 + int(s[i])
            
            if (not s[i].isdigit() and s[i]!=' ') or  i==len(s)-1:
                if sign=='+':
                    b.append(rem)
                elif sign=='-':
                    b.append(-rem)
                elif sign=="*":
                    b.append(b.pop() * rem)
                else:
                    b.append(int(b.pop()/ rem))
                sign = s[i]
                rem = 0
        return sum(b)


        
        
        