class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        b = {}
        maxi = 0
        l = 0

        

        for i in range(len(fruits)):
            b[fruits[i]] = b.get(fruits[i],0) + 1

            while(len((b)) > 2):
                b[fruits[l]]-=1
                if b[fruits[l]] ==0:
                    b.pop(fruits[l])
                l = l + 1
            maxi = max(maxi,i-l+1)
            print(maxi)
        return maxi
        