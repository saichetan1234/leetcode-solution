class Solution:
    def makeFancyString(self, s: str) -> str:

        b  = [s[0]]

        count = 1

        for i in range(1,len(s)):
            if s[i-1] == s[i]:
                count = count + 1
            else:
                count = 1
        
            if count <=2:
                b.append(s[i])

        print(b)

        return "".join(b)

    
       

       
       