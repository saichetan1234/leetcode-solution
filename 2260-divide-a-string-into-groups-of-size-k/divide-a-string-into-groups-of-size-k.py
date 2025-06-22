class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        b = []
        for i in range(0,len(s),k):
            ans = s[i:i+k]

            if len(ans) <k:
                ans = ans+fill*(k-len(ans))
            b.append(ans)
        return b

            
            

        print(ans)
            
        