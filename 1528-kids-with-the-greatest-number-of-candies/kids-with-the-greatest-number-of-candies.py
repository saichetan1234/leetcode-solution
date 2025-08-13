class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxi = max(candies)

        c = []

        for i in candies:
            c.append(i+extraCandies)
        print(c)

        b = []
        for i in c:
            if i>=maxi:
                b.append(True)
            else:
                b.append(False)
        print(b)
        return b