class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:

        m = len(mat)
        n = len(mat[0])

        l = 0
        h = n-1

        while(l<=h):
            mid = (l+h)//2
            maxi = -1
            index = -1
            for i in range(0,m):
                if(mat[i][mid] > maxi):
                    maxi = mat[i][mid]
                    index = i
            
            if mid-1>=0:
                left = mat[index][mid-1]
            else:
                left = -1
            if mid+1<=n-1:
                right = mat[index][mid+1]
            else:
                right  = -1
            
            if left>mat[index][mid]:
                h = mid -1
            elif right>mat[index][mid]:
                l = mid + 1
            else:
                return [index,mid]
        return [-1,-1]



                


        
            
        