class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        strs = sorted(strs)
        n = len(strs)
        first  = strs[0]
        last = strs[n-1]
        print(first)
        print(last)

        ans = ""
        for i in range(len(first)):
            if first[i] == last[i]:
                ans = ans + first[i]
            else:
                return ans 
        
        
                
        return ans
        





        
        
