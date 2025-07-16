class Solution:
    def processStr(self, s: str) -> str:
        res = []

        for i in s:
            if i.islower():
                res.append(i)
            elif i == "#":
                res = res + res
            elif i == "*" and len(res) > 0:
                res.pop()
            else:
                res = res[::-1]
        return "".join(res)
        