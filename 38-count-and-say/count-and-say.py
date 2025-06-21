class Solution:
    def countAndSay(self, n: int) -> str:
        ans="1"
        for i in range(n-1):
            temp=""
            count=1
            for j in range(1,len(ans)+1):
                if j==len(ans) or ans[j-1]!=ans[j]:
                    temp+=str(count)+str(ans[j-1])
                    count=1
                else:
                    count+=1
            ans=temp
        return ans
        


        