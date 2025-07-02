class Solution(object):
    def maxArea(self, height):
        l=0
        r=len(height)-1
        maxi=0
        while l<r:
            if height[l]<height[r]:
                maxi=max(maxi,(r-l)*height[l])
                l+=1
            else:
                maxi=max(maxi,(r-l)*height[r])
                r-=1
        return maxi
        