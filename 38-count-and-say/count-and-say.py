class Solution:
    def countAndSay(self, n: int) -> str:
        
        b= "1"
        for i in range(n-1):
            temp = ""
            count = 1
            for j in range(1,len(b)+1):
                if(j==len(b) or b[j-1]!=b[j]):
                    temp += str(count) + str(b[j-1])
                    count= 1
                else:
                    count = count + 1
            b = temp
        return b 
        