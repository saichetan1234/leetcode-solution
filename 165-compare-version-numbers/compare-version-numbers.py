class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:

        c = version1.split(".")
        print(c)
        d = version2.split(".")
        print(d)

        
        
        e = [int(x) for x in c]
        f = [int(x) for x in d]

        print(e)
        print(f)

        
        
        n = max(len(e), len(f))
        for i in range(n):
            v1 = e[i] if i < len(e) else 0
            v2 = f[i] if i < len(f) else 0
            if v1 < v2:
                return -1
            elif v1 > v2:
                return 1
        return 0
