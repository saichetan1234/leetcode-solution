class Solution:
    def kthCharacter(self, k: int) -> str:

        ans = 'a'


        while(len(ans) < k):
            b= ''
            for i in ans:
                b =b + chr(ord(i)+1)
            ans = ans + b
        return ans[k-1]
            
        

        