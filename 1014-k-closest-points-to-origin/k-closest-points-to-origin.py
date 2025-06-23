class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = []
        for i in points:
            x,y =i
            
            distance = pow(x,2)+pow(y,2)
            dist.append((distance,i))
        print(dist) 

        dist.sort()

        ans = dist[:k]
        print(ans)  

        result = []

        for i,j in ans:
            result.append(j)
        print(result)   
        return result  