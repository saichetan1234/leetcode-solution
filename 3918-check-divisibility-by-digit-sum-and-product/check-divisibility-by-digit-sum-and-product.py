class Solution:
    def checkDivisibility(self, n: int) -> bool:
        rem = 0
        sumi = 0
        prod = 1
        rem1 = 0
        m = n
        s = n


        while n >0:
            rem= n%10
            sumi = sumi + rem
            n = n//10
        print(sumi)

        

        while m >0:
            rem1= m%10
            prod = prod * rem1
            m = m//10
        print(prod)

        ans = prod + sumi

        if s % ans ==0:
            return True
        else:
            return False



        
        
        
        