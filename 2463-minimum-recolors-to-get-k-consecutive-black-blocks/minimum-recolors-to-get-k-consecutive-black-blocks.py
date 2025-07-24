class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        b = []
        count = 0 
        l = 0
        ans = float('inf')

        for r in range(len(blocks)):
            if blocks[r] == 'B':
                count = count + 1
            while(r-l+1 > k):
                
                if blocks[l] == 'B':
                    count-=1
                l = l + 1

            
            if r-l+1 ==k:

                ans = min(ans,k - count)
        return ans



        