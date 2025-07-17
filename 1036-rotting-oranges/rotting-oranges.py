from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        fresh = 0
        rows = len(grid)
        cols = len(grid[0])
        q = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r,c))
                elif grid[r][c] ==1:
                    fresh = fresh + 1
        
        minutes = 0
        direction = [(0,-1),(0,1),(-1,0),(1,0)]

        while q and fresh>0:
            for i in range(len(q)):
                r,c  = q.popleft()
                for dr,dc in direction:
                    nr ,nc = r+ dr,c + dc
                    if 0<=nr<rows and 0<=nc<cols and grid[nr][nc] == 1:
                        grid[nr][nc] =2
                        fresh = fresh -1
                        q.append((nr,nc))
            minutes =  minutes + 1

        if fresh == 0:
            return minutes
        else:
            return -1
        