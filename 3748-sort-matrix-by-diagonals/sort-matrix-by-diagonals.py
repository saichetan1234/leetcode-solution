class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        temp ={}

        for i in range(m):
            for j in range(n):
                if i - j  not in temp:
                    temp[i-j] = []
                temp[i-j].append(grid[i][j])
        print(temp)

        for key,value in temp.items():
            if key>=0:
                temp[key].sort(reverse = True)
            else:
                temp[key].sort()
        print(temp)
        print(temp[0])


        for i in range(m):
            for j in range(n):
                grid[i][j] = temp[i-j].pop(0)
        return grid 

       
       