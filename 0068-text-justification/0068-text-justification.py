
class Solution(object):
    def fullJustify(self, words, maxWidth):
        result = []
        i = 0
        n = len(words)

        while i < n:
            j = i
            letters = 0

            # Greedily fit as many words as possible
            while j < n and letters + len(words[j]) + (j - i) <= maxWidth:
                letters += len(words[j])
                j += 1

            num_words = j - i
            num_spaces = maxWidth - letters

            # Last line or a line with only one word
            if j == n or num_words == 1:
                line = " ".join(words[i:j])
                line += " " * (maxWidth - len(line))

            else:
                gaps = num_words - 1
                spaces_per_gap = num_spaces // gaps
                extra_spaces = num_spaces % gaps

                line = ""

                for k in range(i, j - 1):
                    line += words[k]
                    line += " " * spaces_per_gap

                    if k - i < extra_spaces:
                        line += " "

                line += words[j - 1]

            result.append(line)
            i = j

        return result
