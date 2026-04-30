class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:

        maxi = 0
        total_c = 0
        l = 0

        for r in range(len(s)):
            total_c += abs(ord(s[r])  - ord(t[r]))

            while total_c > maxCost:
                total_c -= abs(ord(s[l])  - ord(t[l]))
                l = l +1
            maxi = max(maxi,r-l+1)
        return maxi