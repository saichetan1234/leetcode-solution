class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:

        res = []

        def bactrack(start,path):
            res.append(path[:])

            for i in range(start,len(nums)):
                path.append(nums[i])
                bactrack(i+1,path)
                path.pop()
        
        bactrack(0,[])
        

        b = []

        for i in res:
            if i:
                ans = 0
                for j in i:
                    ans = ans | j
                b.append(ans)
        print(b)


        temp = {}
        c = []
        d = []

        for i in b:
            temp[i] = temp.get(i,0)+1
        
        for key,value in temp.items():
            d.append(value)
        
        ans1 = max(d)
        return ans1
        
        for key,value in temp.items():
            if value == ans1:
                c.append(key)
        print(c)

        