class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

     


        while len(stones) >1:
            stones.sort()
            x = stones.pop()
            y  = stones.pop()

            if x!=y:
                stones.append(x-y)
            elif x == y:
                stones.append(0)
        return stones[0]

            