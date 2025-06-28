
class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        result = 0
        sign = 1
        num = 0

        for char in s:
            if char.isdigit():
                num = num*10 + int(char)
            elif char == "+":
                result += sign*num
                sign = 1
                num = 0
            elif char == "-":
                result += sign*num
                sign = -1
                num = 0
            elif char == "(":
                stack.append(result)
                stack.append(sign)
                result = 0
                sign = 1
            elif char == ")":
                result += num*sign
                
                result = result*stack.pop()
                result += stack.pop()
                num = 0
        return result + sign*num
            