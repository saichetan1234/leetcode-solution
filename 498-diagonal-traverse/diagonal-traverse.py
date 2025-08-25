class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:

        m = len(mat)
        n  = len(mat[0])
        b = []
        c = []
        temp ={}


        for i in range(m):
            for j in range(n):
                if (i+j) not in temp:
                    temp[i+j]=[]
                temp[i+j].append(mat[i][j])
            print()
        for key,values in temp.items():
            if key %2 ==0:
                c.extend(values[::-1])
            else:
                c.extend(values)
        return c



        


        