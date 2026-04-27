class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen = set()
        repeated = set()

        for i in range(len(s) - 10 + 1):
            seq = s[i: i + 10]

            if seq in seen:
                repeated.add(seq)
            else:
                seen.add(seq)

        return list(repeated)