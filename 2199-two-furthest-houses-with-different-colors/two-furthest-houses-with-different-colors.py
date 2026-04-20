class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        b = []
        for i in range(len(colors)):
            for j in range(len(colors)):
                if colors[i] !=colors[j]:
                    b.append(abs(i-j))

        return max(b)
