class Solution(object):
    def isSubsequence(self, s, t):
        
        prt_s = 0
        prt_t = 0

        while prt_s < len(s) and prt_t < len(t):
            if s[prt_s] == t[prt_t]:
                prt_s += 1

            prt_t += 1

        return prt_s == len(s)