class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = 'aeiouAEIOU'
        b=[]
        c=[]
        d =[]
        for i in s:
            b.append(i)
        print(b)


        for i in b:
            if i in vowels:
                c.append(i)
        print(c)
          

        for i in c[::-1]:
            d.append(i)
        print(d)
        
        

        j = 0

        for i in range(len(b)):
            if b[i] in vowels:
                b[i] = d[j]
                j = j +1
        return "".join(b)



        



       
        
        