class Solution:
    def reorganizeString(self, s: str) -> str:

        temp = {}

        for i in s:
            temp[i] = temp.get(i,0) + 1
        print(temp)

        ans  = max(temp,key=temp.get)
        print(ans)

        if temp[ans]>(len(s)+1)/2:
            return ""

        res = [""]*len(s)
        i = 0

        while temp[ans]>0:
            res[i] = ans
            i = i +2
            temp[ans]-=1

        print(res)
        print(temp)
        print(i)

        for key in temp:
            while temp[key]>0:
                if i >= len(s):
                    i = 1
                res[i] = key
                i = i + 2
                temp[key]-=1
        
        print(res)
        return "".join(res)



        