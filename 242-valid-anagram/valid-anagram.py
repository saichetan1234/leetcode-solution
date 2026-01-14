class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ans = sorted(s)
        ans1 = sorted(t)

        if ans == ans1:
            return True
        else:
            return False
            