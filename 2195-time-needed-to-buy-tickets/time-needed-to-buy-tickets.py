class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:

        b = []
        c = 0
        for i in range(0,len(tickets)):
            b.append([i,tickets[i]])
        print(b)

        while b:
            ans = b.pop(0)
            ans[1]-=1
            c = c + 1

            if ans[1] == 0 and ans[0] == k:
                return c
            
            if ans[1]>0:
                b.append(ans)

            

    


        