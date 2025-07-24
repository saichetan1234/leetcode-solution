class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l=0
        count=0
        ans=float('inf')
        for r in range(len(blocks)):
            if blocks[r]=="B":
                count+=1
            while r-l+1>k:
                if blocks[l]=="B":
                    count-=1
                l+=1
            if r-l+1==k:
                ans=min(ans,k-count)
        return ans
        