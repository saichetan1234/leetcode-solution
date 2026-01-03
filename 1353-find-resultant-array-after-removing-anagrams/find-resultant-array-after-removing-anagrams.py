class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
       
        prev =""
        res = []

        for i in range(len(words)):
            ans = ''.join(sorted(words[i]))

            if ans!=prev:
                res.append(words[i])
                prev = ans
        print(res)
        return res

        




      

        

    
        