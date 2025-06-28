class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)  

        
        nidx = []
        for i in range(n):
            pair = (nums[i], i)
            nidx.append(pair)

        
        nidx.sort(reverse=True) 

     
        top_k_pairs = nidx[:k]

        
        top_k_pairs.sort(key=lambda info: info[1])

        
        result = []
        for info in top_k_pairs:
            result.append(info[0])

        return result
