class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        b = []

        for i in s:
            b.append(ord(i))
        print(b)
        
        c = []

        for i in t:
            c.append(ord(i))
        print(c)

        if len(b)!=len(c):
            return False
        else:
            temp = {}

            for i in range(len(b)):
                key = b[i]
                value = c[i]

                if key in temp:
                    if temp[key]!=value:
                        return False
                else:
                    if value in temp.values():
                        return False

                    temp[key] = value
            return True   


        

        
        