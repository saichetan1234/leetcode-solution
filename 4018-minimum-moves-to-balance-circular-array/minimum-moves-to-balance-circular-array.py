class Solution:
    def minMoves(self, balance: List[int]) -> int:

        ans = sum(balance)
        n = len(balance)

        if ans <0:
            return -1
        
        neg_idx = -1
        for i in range(len(balance)):
            if balance[i]<0:
                neg_idx = i
                break
        if neg_idx ==-1:
            return 0

        need = -balance[neg_idx]
        b = []
        
        for i in range(len(balance)):
            if i !=neg_idx and balance[i]>0:
                dist = min(abs(i-neg_idx),n-abs(i-neg_idx))
                b.append((dist,balance[i]))
        print(b)
       
        b.sort() 
        print(b)
        moves = 0

        for dist,val in b:
            take = min(val,need)
            moves = moves + take * dist
            need = need - take 
            if need  ==0:
                break
        return moves