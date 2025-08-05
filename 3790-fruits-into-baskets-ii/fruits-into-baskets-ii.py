class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:

        for i in range(len(fruits)):
            for j in range(len(baskets)):
                if fruits[i]<=baskets[j]:
                    baskets.pop(j)
                    break
        print(baskets)
        return len(baskets)
        