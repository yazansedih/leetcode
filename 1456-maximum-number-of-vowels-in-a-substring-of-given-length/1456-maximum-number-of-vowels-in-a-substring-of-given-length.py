class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        vowels = ['a', 'e', 'i', 'o', 'u']

        count_vowels = 0
        window = s[0: k] 

        for char in window:
            if char in vowels:
                count_vowels += 1

        max_vowels = count_vowels

        for i in range(k, len(s)):
            
            if s[i] in vowels:
                count_vowels += 1

            if s[i - k] in vowels:
                count_vowels -= 1

            max_vowels = max(max_vowels, count_vowels)

            if max_vowels == k:
                return k

        return max_vowels