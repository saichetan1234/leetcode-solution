class Solution:
    def findMaxLength(self, nums: List[int]) -> int:

        b = []
        k = 0
        hashmap = {}
        sumi = 0
        maxi = 0

        for i in nums :
            if i ==0:
                b.append(-1)
            else:
                b.append(1)
        print(b)


        for i in range(len(b)):
            sumi = sumi + b[i]

            if sumi==k:
                maxi =  max(maxi,i+1)

            if sumi-k in hashmap:
                maxi = max(maxi,i-hashmap[sumi-k])

            if sumi not in hashmap:
                hashmap[sumi] = i

        return maxi


           
           