class Solution(object):
    def isValid(self, s):
        stack = []

        pairs = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for char in s:

            # Opening bracket
            if char not in pairs: 
                stack.append(char)

            # Closing bracket
            else:
                if not stack or stack.pop() != pairs[char]:
                    return False

        return len(stack) == 0