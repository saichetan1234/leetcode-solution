class Solution:
    def limitOccurrences(self, nums: list[int], k: int) -> list[int]:

        b = ""
        temp = {}
        c = []

        for i in nums:
            temp[i] = temp.get(i,0) + 1
        
        print(temp)

        for key,value in temp.items():
            if value > k:
                temp[key]=k
        print(temp)

        for key,value in temp.items():
            for i in range(value):
                c.append(key)
        return c
        