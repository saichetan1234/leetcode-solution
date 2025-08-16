class Solution:
    def largestGoodInteger(self, num: str) -> str:
        b= []
        n = len(num)

        for i in range(n):
            for j in range(i+1,n):
                b.append(num[i:j+1])
       

        c = []

        for i in b:
            if len(i)==3:
                c.append(i)
        

        d = []

        for i in c:
            if i == i[::-1] and i[0] == i[1]==i[2]:
                d.append(i)
       
       

        d=sorted(d)
        if len(d)>0:
            return d[-1]
        else:
            return ""
        

       
       