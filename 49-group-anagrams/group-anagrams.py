class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        b = []
        for i in strs:
            asw = "".join(sorted(i))
            b.append(asw)
        print(b)

        temp = defaultdict(list)

        

        for i ,j in zip(b,strs):
            temp[i].append(j)
            
        
        return list(temp.values())

    
    