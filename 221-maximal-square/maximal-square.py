class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:

        m = len(matrix)
        n = len(matrix[0])

        dp = [[0 for i in range(n)] for j in range(m)]

        for i in range(m):
            for j in range(n):
                if matrix[i][j] =='1':
                    if i=='0' or j =='0':
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1]) + 1
        print(dp)
        

        maxi = float('-inf')

        for i in dp:
            for j in i:
                num = int(j)

                if num > maxi:
                    maxi = num
        print(maxi)

        return maxi * maxi