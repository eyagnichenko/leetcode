"""
https://leetcode.com/problems/number-of-digit-one/
Beats 100% by runtime, 90+% by memory.

Tested for 0 <= n <= 10 ** 9 (original LeetCode's constraints).

For higher n values, some code adjustments are needed to avoid calculation bugs caused by dynamic typing.
"""
class Solution:

    def countDigitOne(self, n: int) -> int:

        if n < 1:
            return 0

        if n == 1:
            return 1

        count = 0
        while n > 0:
            x = len(str(n)) - 1
            a = n // 10 ** x
            n -= a * 10 ** x
            if a == 1:
                count += x * 10 ** (x - 1) + 1 + n
            else:
                count += 10 ** x + 10 ** (x - 1) * a * x

        return int(count)