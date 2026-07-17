class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort(key = lambda x:(x[0],-x[-1]))
        b = []
        maxi = 0

        for i in intervals:
            if not b:
                b.append(i)
                maxi = i[1]
            
            elif i[1]>maxi:
                b.append(i)
                maxi = i[1]
        return len(b)

        