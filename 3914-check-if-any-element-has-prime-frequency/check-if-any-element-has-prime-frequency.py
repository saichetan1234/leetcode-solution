class Solution:
    def checkPrimeFrequency(self, nums: List[int]) -> bool:

        b = []
        temp = {}
        c = []

        for i in nums:
            temp[i] = temp.get(i,0)+1
        
        for key,value in temp.items():
            b.append(value)
        print(b)

        for i in b:
            flag = False
            if i<=1:
                flag = True
            else:


                for j in range(2,int(i**0.5)+1):
                    if i%j==0:
                        flag = True
                        break
            if flag ==False:
                c.append("Prime")
            else:
                c.append("Not_prime")
        print(c)
        count = 0

        for i in c:
            if i=='Prime':
                count = count +1
        print(count)

        if count>=1:
            return True
        else:
            return False
            

        