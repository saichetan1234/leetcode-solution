class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        sumi = 0
        hashmap  = {0:1}
        count  = 0

        for i in nums:
            sumi  =  sumi + i 

            if sumi - k in hashmap:
                count  =  count + hashmap[sumi-k ]
            
            hashmap[sumi] = hashmap.get(sumi,0)+1

        return count
        
        