class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits=="":
            return []
        phone={"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        ans=[]
        n=len(digits)
        def backtrack(index,path):
            if index==n:
                if "".join(path) not in ans:
                    ans.append("".join(path))
                return 
            for i in phone[digits[index]]:
                path.append(i)
                backtrack(index+1,path)
                path.pop()
        backtrack(0,[])
        return ans
        