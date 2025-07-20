class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:

        rows  = len(mat)
        cols = len(mat[0])

        dist = [[float('inf') for i in range(cols)] for j in range(rows)]

        queue = deque()

        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    dist[r][c] = 0
                    queue.append((r,c))
        
        direction = [(0,1),(-1,0),(0,-1),(1,0)]

        while queue :
            for i in range(len(queue)):
                r,c = queue.popleft()

                for dr,dc in direction:
                    nr,nc = r + dr,c + dc 

                    if 0<=nr< rows and 0<=nc<cols :
                        if dist[nr][nc] > dist[r][c] :
                            dist[nr][nc] = dist[r][c] + 1
                            queue.append((nr,nc))
        return dist

       