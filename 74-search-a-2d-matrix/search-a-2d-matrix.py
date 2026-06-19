class Solution(object):
    def searchMatrix(self, matrix, target):
        
        if not matrix or not matrix[0]:
            return False
        
        m = len(matrix)
        n = len(matrix[0])

        i = 0
        j = n-1

        while i<=m-1 and j>=0:
            if matrix[i][j]==target:
                return True
            
            if matrix[i][j]>target:
                j = j -1 
            else:
                i = i + 1
        return False


       
       