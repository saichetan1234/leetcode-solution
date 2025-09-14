class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        maxi=float('inf')

        for i in tasks:
            if sum(i)<maxi:
                maxi=sum(i)
        return maxi
            
        