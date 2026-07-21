class Solution:
    def smallestSubsequence(self, s: str) -> str:
        temp={}

        for i in s:
            temp[i] = temp.get(i,0) + 1
        
        b = []
        visited = set()

        for i in s:
            temp[i]-=1
            if i in visited:
                continue
            
            while b and b[-1]>i and temp[b[-1]]>0:
                visited.remove(b.pop())
            
            b.append(i)
            visited.add(i)
        return "".join(b)


       
       
      

               