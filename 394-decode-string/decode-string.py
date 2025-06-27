class Solution:
    def decodeString(self, s: str) -> str:
        alpa = []
        i=0
        while i<len(s):
            nm=""
            while s[i].isdigit():
                nm+=s[i]
                i+=1
            if nm!="" :
                alpa.append(int(nm))
            if s[i]!=']':
                alpa.append(s[i])
            else:
                temp = ""
                while(alpa[-1]!='['):
                    temp = alpa[-1]+temp
                    alpa.pop()
                alpa.pop()
                temp2 = alpa.pop()
                alpa.append(temp2*temp)
            i+=1
        return "".join(alpa)
        