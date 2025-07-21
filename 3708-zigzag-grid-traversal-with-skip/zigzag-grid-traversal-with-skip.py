class Solution:
    def zigzagTraversal(self, grid: List[List[int]]) -> List[int]:

        b = []
        for i in range(len(grid)):
            if i %2 == 0:
                b.extend(grid[i])
            else:
                b.extend(grid[i][::-1])
        print(b)

        c = []

        for i in range(len(b)):
            if i%2==0:
                c.append(b[i])
        return c


        
        

      
      