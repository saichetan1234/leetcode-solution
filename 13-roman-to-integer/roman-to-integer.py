class Solution:
    def romanToInt(self, s: str) -> int:

        temp = {'I':1,'V':5,'X': 10,'L': 50,'C':100,'D':500,'M':1000}
        count  = 0

        for i in range(len(s)-1):
            if temp[s[i]]<temp[s[i+1]]:
                count  = count - temp[s[i]]
            else:
                count  = count +  temp[s[i]]
        count  =  count + temp[s[-1]]
        return count
        