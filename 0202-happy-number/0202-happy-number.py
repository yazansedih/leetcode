class Solution(object):
    def isHappy(self, n):
        seen = set()

        while n != 1 and n not in seen:
            seen.add(n)
            sum_pow = 0

            while n > 0:
                digit = n % 10
                sum_pow += digit ** 2
                n //= 10

            n = sum_pow

        return n == 1