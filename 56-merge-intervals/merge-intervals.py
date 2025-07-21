class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort()

        b=[]

        for i in intervals:
            if not b or b[-1][1] < i[0]:
                b.append(i)
            else:
                b[-1][1] = max(i[1],b[-1][1])
        return b

        