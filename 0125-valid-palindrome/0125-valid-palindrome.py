class Solution(object):
    def isPalindrome(self, s):
        
        s = ''.join(char for char in s.lower() if char.isalnum())

        left = 0
        right = len(s) - 1

        while left < right:

            if s[left] != s[right]:
                return False

            left += 1
            right -= 1
        
        return True
