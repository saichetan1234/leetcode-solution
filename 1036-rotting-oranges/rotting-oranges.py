from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        fresh = 0
        row  = len(grid)
        col = len(grid[0])

        for r in range((row)):
            for c in range((col)):
                if grid[r][c] == 2:
                    q.append((r,c))
                elif grid[r][c] == 1:
                    fresh = fresh + 1
        minutes = 0
        direct = [(0,1),(1,0),(0,-1),(-1,0)]

        while q and fresh >0:
            for i in range(len(q)):
                r,c = q.popleft()
                for dr,dc in direct:
                    nr = r + dr
                    nc = c + dc 

                    if 0<=nr<row and 0<=nc<col and grid[nr][nc] ==1:
                        grid[nr][nc] =2
                        fresh = fresh -1
                        q.append((nr,nc))
            minutes = minutes + 1
        
        if fresh ==0:
            return minutes
        else:
            return -1




        
        