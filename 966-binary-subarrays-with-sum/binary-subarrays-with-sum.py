class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        
        maps = {0:1}
        count = 0
        sumi = 0

        for i in nums:
            sumi = sumi + i

            if sumi - goal in maps:
                count  =  count + maps[sumi - goal]

            maps[sumi] = maps.get(sumi,0) + 1

        return count