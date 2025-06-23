class Solution:
    def countServers(self, grid: List[List[int]]) -> int:

        m = len(grid)
        n = len(grid[0])

        row_c = [0]*m 
        col_c = [0]*n 

        for i in range(m):
            for j in range(n):
                if grid[i][j] ==1:
                    row_c[i]=row_c[i]+1
                    col_c[j] = col_c[j] + 1
        print(row_c)   
        print(col_c)

        c = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] ==1 and(row_c[i]>1 or col_c[j]>1):
                    c = c+1
        return c