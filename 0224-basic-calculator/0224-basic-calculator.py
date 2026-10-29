class Solution(object):
    def calculate(self, s):
        stack = []
        result = 0
        num = 0
        sign = 1

        for char in s:
            if char.isdigit():
                num = num * 10 + int(char)

            elif char == '+':
                result += sign * num
                num = 0
                sign = 1

            elif char == '-':
                result += sign * num
                num = 0
                sign = -1

            elif char == '(':
                stack.append(result)
                stack.append(sign)

                result = 0
                sign = 1

            elif char == ')':
                result += sign * num
                num = 0

                result *= stack.pop()
                result += stack.pop()

        return result + sign * num