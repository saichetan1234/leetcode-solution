class Solution:
    def mirrorDistance(self, n: int) -> int:

        sumi = 0
        temp = n
        while temp >0:
            rem = temp %10
            sumi  = sumi * 10 + rem 
            temp = temp//10
        
        return abs(n-sumi)


        