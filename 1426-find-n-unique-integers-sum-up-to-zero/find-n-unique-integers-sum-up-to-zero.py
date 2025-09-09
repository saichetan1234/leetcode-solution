class Solution:
    def sumZero(self, n: int) -> List[int]:
        b = []
        for i in range(1,n//2+1):
            b.append(i)
            b.append(-i)
        

        if n%2!=0:
            b.append(0)
        print(b)

        return b

        