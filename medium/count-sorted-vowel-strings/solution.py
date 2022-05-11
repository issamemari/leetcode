import operator as op
from functools import reduce


class Solution:
    def ncr(self, n, r):
        r = min(r, n - r)
        numer = reduce(op.mul, range(n, n - r, -1), 1)
        denom = reduce(op.mul, range(1, r + 1), 1)
        return numer // denom

    def countVowelStrings(self, n: int) -> int:
        return self.ncr(n + 4, n)
