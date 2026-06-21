class Solution:
    def reverseWords(self, s: str) -> str:
        b = []
        c = []

        for i in s.split():
            b.append(i)
        print(b)

        for i in b[::-1]:
            c.append(i)
        print(c)

        return " ".join(c)
        