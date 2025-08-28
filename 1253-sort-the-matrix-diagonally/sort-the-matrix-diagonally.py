class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:

        temp = {}
        m = len(mat)
        n = len(mat[0])

        for i in range(m):
            for j in range(n):
                if i-j not in temp:
                    temp[i-j] = []
                temp[i-j].append(mat[i][j])
        print(temp)

        for key , value in temp.items():
            if key >=0:
                temp[key].sort()
            else:
                temp[key].sort()
        print(temp)

        for i in range(m):
            for j in range(n):
                mat[i][j] = temp[i-j].pop(0)
        return mat
        