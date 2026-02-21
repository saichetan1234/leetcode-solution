class Solution:
    def reverseBits(self, n: int) -> int:
        b = []
        for i in range(32):
            b.append(n%2)
            n=n//2
       
        ans = "".join(str(x) for x in b)
        print(ans)

        power = 0
        temp = 0

        for i in range(len(ans)-1,-1,-1):
            temp = temp + (int(ans[i]) * (2 ** power))
            power  =  power + 1
        return temp






