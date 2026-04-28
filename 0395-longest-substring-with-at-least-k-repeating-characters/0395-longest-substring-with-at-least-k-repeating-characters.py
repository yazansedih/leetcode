from collections import Counter

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) < k:
            return 0

        freq = Counter(s)

        for ch in freq:
            if freq[ch] < k:
                parts = s.split(ch)
                return max(self.longestSubstring(part, k) for part in parts)

        return len(s)