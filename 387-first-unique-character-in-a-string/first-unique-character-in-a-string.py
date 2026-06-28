class Solution:
    def firstUniqChar(self, s: str) -> int:
        temp={}
        c = []

        for i in s:
            temp[i] = temp.get(i,0)+ 1
        print(temp)
        
        for key,value in temp.items():
            if value == 1:
                c.append(key)
        print(c)
        if len(c)>=1:
            ans = c[0]
        else:
            return -1
        print(ans)

        for i in range(0,len(s)):
            if s[i] == ans:
                return i
            

        
        
        