class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:

        maxi = 0
        maxi_freq = 0

        temp = {}
        l = 0

        for r in range(0,len(answerKey)):
            temp[answerKey[r]] = temp.get(answerKey[r],0) + 1
            maxi_freq = max(maxi_freq,temp[answerKey[r]])

            while (r-l+1  - maxi_freq>k ):
                temp[answerKey[l]] -=1
                l = l +1
            maxi = max(maxi,r-l+1)
        return maxi
        