class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        

        m = len(image)
        n = len(image[0])

        ans = [[ 0 for j in range(n)] for i in range(m)]

        for i in range(m):
            for j in range(n):
                ans[i][j] = image[i][j]
        print(ans)

        orginal = ans[sr][sc]

        if orginal == color:
            return ans


        def dfs(r,c):

            if r <0 or c <0 or r >=m or c >=n:
                return 
            
            if ans[r][c]!=orginal:
                return 

            ans[r][c] = color
            
            dfs(r-1,c)
            dfs(r+1,c)
            dfs(r,c-1)
            dfs(r,c+1)
        
        dfs(sr,sc)
        return ans
