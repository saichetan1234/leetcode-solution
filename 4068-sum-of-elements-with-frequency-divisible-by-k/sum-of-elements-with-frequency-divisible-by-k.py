class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:
        temp = {}
        b = []
        c = []

        for i in nums:
            temp[i] = temp.get(i,0) + 1
        print(temp)

        for key,value in temp.items():
            if value % k ==0:
                b.append(key)
        print(b)

        for i in nums:
            for j in b:
                if i == j:
                    c.append(i)
        print(c)

        if len(c) == 0:
            return 0
        else:
            return sum(c)
