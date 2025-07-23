class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        s1=[]
        s2=[]
        ans1=0
        ans2=0
        if x>y:
            for i in s:
                if i=="b" and s1 and s1[-1]=="a":
                    s1.pop()
                    ans1+=x
                else:
                    s1.append(i)
            str2="".join(s1)
            s11=[]
            for i in str2:
                if i=="a" and s11 and s11[-1]=="b":
                    s11.pop()
                    ans1+=y
                else:
                    s11.append(i)
            return ans1
        else:
            for i in s:
                if i=="a" and s2 and s2[-1]=="b":
                    s2.pop()
                    ans2+=y
                else:
                    s2.append(i)
            str3="".join(s2)
            s22=[]
            for i in str3:
                if i=="b" and s22 and s22[-1]=="a":
                    s22.pop()
                    ans2+=x
                else:
                    s22.append(i)
            return ans2
        
        