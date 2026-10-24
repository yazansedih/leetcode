class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False

        s_map = {}
        t_map = {}

        for i in range(len(s)):
            if s[i] in s_map:
                s_map[s[i]] += 1
            else:
                s_map[s[i]] = 1

        for i in range(len(t)):
            if t[i] in t_map:
                t_map[t[i]] += 1
            else:
                t_map[t[i]] = 1

        return s_map == t_map
