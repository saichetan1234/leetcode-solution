class Solution:
    def maxSum(self, nums: List[int]) -> int:

        temp = list(set(nums))

        temp.sort()
        if temp[-1] <0:
            return temp[-1]
        print(temp)
        b = []
        for i in temp:
            if i >0:
                b.append(i)
        print(sum(b))
        return sum(b)


        