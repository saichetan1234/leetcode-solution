class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        left = [1]*n
        for i in range(1,len(ratings)):
            if ratings[i]>ratings[i-1]:
                left[i] = left[i-1]+1
        for i in range(n-2,-1,-1):
            if ratings[i]> ratings[i+1]:
                left[i] = max(left[i],left[i+1] +1)
        return sum(left)

        
        