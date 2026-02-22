class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:


        sumi = 0
        hasmap = {0:1}
        count  = 0

        for i in nums :
            sumi =  sumi +i 

            if (sumi % k + k)%k  in hasmap:
                count  =  count + hasmap[(sumi %k +k)%k]

            hasmap[(sumi % k + k) % k] =  hasmap.get((sumi % k + k) % k,0) + 1

        return count


       
       