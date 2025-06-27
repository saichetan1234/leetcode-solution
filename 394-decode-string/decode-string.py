class Solution:
    def decodeString(self, s: str) -> str:
        num = []
        alpa = []
        i=0
        while i<len(s):
            nm=""
            while s[i].isdigit():
                nm+=s[i]
                i+=1
            if nm!="" :
                num.append(int(nm))
            if s[i]!=']':
                alpa.append(s[i])
            else:
                temp = ""
                while(alpa[-1]!='['):
                    temp = alpa[-1]+temp
                    alpa.pop()
                alpa.pop()
                temp2 = num.pop()
                alpa.append(int(temp2)*temp)
            i+=1
        print(alpa)
        return "".join(alpa)
        