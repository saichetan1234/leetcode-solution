class Solution:
    def isPalindrome(self, s: str) -> bool:
        ans = s.split()
        print(ans)

        temp = "".join(ans)
        print(temp)
        temp1 = ""

        for i in temp:
            if i.isalnum():
                temp1 = temp1+i
        print(temp1)
        temp2 = temp1.lower()
        print(temp2)

        if temp2 == temp2[::-1]:
            return True
        else:
            return False
       
       