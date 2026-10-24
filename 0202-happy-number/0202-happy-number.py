class Solution(object):
    def isHappy(self, n):
        seen = set()

        while n != 1 and n not in seen:
            seen.add(n)
            happy_sum = 0

            while n > 0:
                digit = n % 10
                happy_sum += digit ** 2
                n //= 10

            n = happy_sum

        return n == 1

            