class Solution:
    def maxDepth(self, s: str) -> int:
        maxi = 0
        count  = 0

        for i in s:
            if i =='(':
                count  =  count + 1

                if maxi<count:
                    maxi = count
            if i == ')':
                count = count -1
        return maxi
        