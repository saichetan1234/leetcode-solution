class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:

        a = []
        a1 = []
        b = []
        b1 = []
        count1 = 0
        count2 = 0

        if x>y:
            for i in s:
                if i == 'b' and a and a[-1] == 'a':
                    a.pop()
                    count1 = count1+x
                else:
                    a.append(i)
            str1 = "".join(a)

            for i in str1:
                if i == 'a' and a1 and a1[-1] == 'b':
                    a1.pop()
                    count1 = count1+y
                else:
                    a1.append(i)
            return count1
        else:
            for i in s:
                if i == 'a' and b and b[-1] == 'b':
                    b.pop()
                    count2 = count2 + y
                else:
                    b.append(i)
            str2 = "".join(b)

            for i in str2:
                if i == 'b' and b1 and b1[-1] == 'a':
                    b1.pop()
                    count2 = count2 + x
                else:
                    b1.append(i)
            return count2



        
    
        