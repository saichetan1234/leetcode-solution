class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        temp = {}
        b = list(map(int , str(n)))
        print(b)
        c = []

        for i in b:
            temp[i] = temp.get(i,0) + 1
        
        for key,value in temp.items():
            c.append(key * value)
        return sum(c)

        
        