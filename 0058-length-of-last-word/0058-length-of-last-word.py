class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        count  = 0

        for i in range(len(s) - 1, -1, -1):
            if s[i] == " ":
                if count > 0:
                    break
                continue

            count += 1

        return count