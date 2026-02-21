class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        count  = 0 
        hasmap = {0:1}
        sumi = 0

        for i in nums:
            sumi = sumi + i

            if sumi - k in hasmap:
                count  = count + hasmap[sumi-k]
            
            hasmap[sumi] = hasmap.get(sumi,0) + 1
        return count

        
        