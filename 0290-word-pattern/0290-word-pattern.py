class Solution(object):
    def wordPattern(self, pattern, s):
        words = s.split(' ')
        patterns = {}
        words_map = {}

        char = 0
        word = 0

        while char < len(pattern) and word < len(words):
            p = pattern[char]
            w = words[word]

            if p in patterns and patterns[p] != w:
                return False

            if w in words_map and words_map[w] != p:
                return False

            patterns[p] = w
            words_map[w] = p

            char += 1
            word += 1

        return char == len(pattern) and word == len(words)