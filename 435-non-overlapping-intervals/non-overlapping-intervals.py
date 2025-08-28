class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

       
        b = []

        for i in intervals:
            if not b or b[-1][1]<=i[0]:
                b.append(i)
            else:
                if i[1] < b[-1][1]:
                    b[-1] = i
        print(b)

        m = len(intervals)
        n = len(b)
        print(m)
        print(n)

        return m-n
        