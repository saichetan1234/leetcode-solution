class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:

        b = []
        sumi = 0

        for i in range(0,k):
            sumi = sumi + arr[i]
        b.append(sumi/k)

        for i in range(k,len(arr)):
            sumi = sumi + arr[i] - arr[i-k]
            b.append(sumi/k)
        print(b)

        c = 0

        for i in b:
            if i >= threshold:
                c = c +1
        return c

        
        