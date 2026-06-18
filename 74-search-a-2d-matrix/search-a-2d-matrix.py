class Solution(object):
    def searchMatrix(self, matrix, target):
        
        if not matrix or not matrix[0]:
            return False
        
        m = len(matrix)
        n = len(matrix[0])

        for i in range(0,m):
            l = 0
            h = n-1
            ans = 0

            while(l<=h):
                mid  = (l+h)//2

                if matrix[i][mid] == target:
                    return True
                elif matrix[i][mid]<target:
                    l = mid + 1
                else:
                    h = mid -1 
        return False

       
       