class Solution:
    def capitalizeTitle(self, title: str) -> str:
        b = title.split()
        print(b)
        c = []

        for i in b:
            if len(i)>=3:
                c.append(i[0].upper() + i[1:].lower())
            else:
                c.append(i.lower())
        print(c)

        return " ".join(c)
        
        