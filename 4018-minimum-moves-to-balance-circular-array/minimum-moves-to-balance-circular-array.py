class Solution:
    def minMoves(self, balance: List[int]) -> int:

        ans = sum(balance)
        n = len(balance)
        # if the sum of the array is negative , then we cant make the array postive 

        if ans <0:
            return -1
        
        neg_idx = -1
        for i in range(len(balance)):
            if balance[i]<0:
                neg_idx = i
                break
        # here i am findiing the negative number's index , if it is -1 then no neg number hence return 0
        if neg_idx ==-1:
            return 0
        # If there is a neg number then we need to find how much wee need from other people to make it positve , like if -4 is there in the arr , we need 4 from other elements to make it positve 
        need = -balance[neg_idx]
        b = []

        # so we need to take  from elements that is not a neg_index and the balance whould be positive hence balance[i] >0
        
        # find the distance to find how many steps are necesary to give it to need elemnet 
        # Since cirular , index 1  -  index 2 one step ,  index 0 - index-1 (step1) index 1-index 2 , step 2 , but as circular we can send index0-index 2 in one step ,and we take the min .
        
        for i in range(len(balance)):
            if i !=neg_idx and balance[i]>0:
                dist = min(abs(i-neg_idx),n-abs(i-neg_idx))
                b.append((dist,balance[i]))
        print(b)

        #to get the best and shortest dist we sort the arr
        # take element from need and val ex , if you need 3 , and you have 2 , then take 2 , another situation is , if you need 5  and you have 10 , then take 5 . 
       
        b.sort() 
        print(b)
        moves = 0

        for dist,val in b:
            take = min(val,need)
            # then cal the moves , take and myltiply with distance , if from first post to thrid pos you need to tranfer 2 units , then u need 4 moves , first - second , second -third for i unit , same for the second so 4 , which is 2 * 2 , 2 is the how much you take and 2 is the dist (3-1)
            moves = moves + take * dist
            need = need - take 
            #after you take , you need to sub from need ,
            #if need becomes 0 , break and return moves
            if need  ==0:
                break
        return moves