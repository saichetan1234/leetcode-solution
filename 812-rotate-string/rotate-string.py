class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        ans = s + s 
        if goal in ans:
            return True
        else:
            return False



    