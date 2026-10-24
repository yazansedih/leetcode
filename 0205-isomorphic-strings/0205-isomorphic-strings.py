class Solution(object):
    def isIsomorphic(self, s, t):

        s_to_t = {}
        t_to_s = {}

        for i in range(len(s)):
            sc = s[i]
            tc = t[i]

            if sc in s_to_t and s_to_t[sc] != tc:
                return False

            if tc in t_to_s and t_to_s[tc] != sc:
                return False

            s_to_t[sc] = tc
            t_to_s[tc] = sc

        return True