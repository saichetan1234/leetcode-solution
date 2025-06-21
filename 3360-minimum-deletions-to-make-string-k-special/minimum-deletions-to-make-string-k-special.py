class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:

        temp = {}

        for i in word:
            temp[i] = temp.get(i,0) +1
        b=sorted(temp.values())
        ans=len(word)
        for i in range(len(b)):
            delete=0
            for j in range(len(b)):
                if b[j]<b[i]:
                    delete+=b[j]
                if b[j]>b[i]+k:
                    delete+=(b[j]-b[i]-k)
            ans=min(ans,delete)
        return ans

                

        
        

        
        