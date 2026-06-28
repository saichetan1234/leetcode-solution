class Solution:
    def frequencySort(self, s: str) -> str:

        temp = {}
        c = []

        for i in s:
            temp[i] = temp.get(i,0) + 1 
        temp_desc = dict(sorted(temp.items(),key = lambda item : item[1],reverse= True))

        print(temp_desc)

        for key , value in temp_desc.items():
            c.append(key * value)
        print(c)

        return "".join(c)
        



        
        