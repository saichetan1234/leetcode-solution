class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        b = []

        l = 0
        r = 0

        while l<len(word1) and r < len(word2):
            b.append(word1[l])
            b.append(word2[r])
            l = l+1
            r = r +1
        
        if len(word2)>len(word1):
            for i in range(r,len(word2)):
                b.append(word2[i])
        else:
            for i in range(l,len(word1)):
                b.append(word1[i])

        
        return "".join(b)


            
        
        
        
        
        
        