from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
       
        q = deque()
        m = len(grid)
        n = len(grid[0])
        fresh = 0
        minutes = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append([i,j])
                elif grid[i][j] == 1:
                    fresh = fresh + 1
        direct = [(0,1),(0,-1),(1,0),(-1,0)]

        while q and fresh > 0:
            for k in range(len(q)):
                i,j = q.popleft()

                for dr,dc in direct:
                    nr,nc = i + dr,j + dc

                    if 0<=nr<m and 0<=nc<n and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh  = fresh -1 
                        q.append([nr,nc])
            minutes = minutes +1
        
        if fresh == 0:
            return minutes
        else:
            return -1



            