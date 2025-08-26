class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        maxi = 0
        prod = 0

        for i in dimensions:
            temp = i[0] * i[0] + i[1] * i [1]

            ans = pow(temp ,1/2)

            if ans > maxi:
                maxi = ans
                prod = i[0] * i[1]
            elif ans==maxi:
                prod=max(prod,i[0]*i[1])
        return prod
            

        
            
        
        
       
       