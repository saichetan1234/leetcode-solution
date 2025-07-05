class Solution:
    def findLucky(self, arr: List[int]) -> int:

        temp ={}
        b =[]

        for i in arr:
            temp[i] = temp.get(i,0) + 1
        for key,value in temp.items():
            if key == value:
                b.append(key)
        print(b)

        if len(b) == 0:
            return -1
        else:
            return max(b)
        