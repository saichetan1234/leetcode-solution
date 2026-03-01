class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sumi = 0
        maps = {0:1}
        count = 0

        for i in nums:
            sumi = sumi + i

            if sumi - k in maps:
                count  =  count + maps[sumi-k]

            maps[sumi] = maps.get(sumi,0) + 1

        return count