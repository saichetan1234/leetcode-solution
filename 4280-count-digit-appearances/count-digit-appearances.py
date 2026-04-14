class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        b = []
        count  = 0

        for i in nums:
            
            sumi = 0
            while i >0:
                rem = i %10
                i  = i //10
                b.append(rem)
        
        for i in b:
            if i ==digit:
                count = count + 1
            
        return count

        