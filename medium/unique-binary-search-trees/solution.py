from functools import lru_cache


class Solution:

    @lru_cache(None)
    def numTrees(self, n: int) -> int:

        if n <= 1:
            return 1

        res = 0
        for i in range(1, n + 1):
            res += self.numTrees(n - i) * self.numTrees(i - 1)

        return res
