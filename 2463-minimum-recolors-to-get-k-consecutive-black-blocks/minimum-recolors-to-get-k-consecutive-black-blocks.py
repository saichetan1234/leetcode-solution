class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
            b = []
            count = 0 

            for i in range(0,k):
                if blocks[i] == 'W':
                    count  = count + 1
                
            b.append(count)

            for i in range(1,len(blocks)-k+1):
                if blocks[i-1] == 'W':
                    count = count -1
                if blocks[i+k-1] == 'W':
                    count  = count + 1
                b.append(count)
            print(b)
            return min(b)
            
                
                
            
        



        