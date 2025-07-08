class Solution:
    def findMaxLength(self, nums: List[int]) -> int:

        b = []
        for i in nums:
            if i ==0:
                b.append(-1)
            else:
                b.append(i)
        print(b)

        seen = {}

        maxi = 0

        sumi = 0

        for i in range(len(b)):
            sumi = sumi + b[i]

            if sumi ==0:
                maxi = i + 1
            
            elif sumi in seen:
                maxi = max(maxi,i-seen[sumi])

            else:
                seen[sumi] = i
        return maxi

       
      