class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        i=0
        minheap=[]
        day=0
        events.sort(key=lambda x:x[0])
        count=0
        n=len(events)
        while i<n or minheap:
            if not minheap:
                day=events[i][0]
            
            while i<n and events[i][0]==day:
                heapq.heappush(minheap,events[i][1])
                i+=1

            while minheap and minheap[0]<day:
                heapq.heappop(minheap)
            
            if minheap:
                heapq.heappop(minheap)
                count+=1
            day+=1
        return count
        