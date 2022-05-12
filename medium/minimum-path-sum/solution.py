from functools import lru_cache
from typing import List


class Solution1:

    @lru_cache(None)
    def minPathSumRecursive(self, i, j) -> int:

        m, n = len(self.grid) - i, len(self.grid[0]) - j

        if m == 1:
            return sum([self.grid[i][j + index] for index in range(n)])
        if n == 1:
            return sum([self.grid[i + index][j] for index in range(m)])

        s1 = self.minPathSumRecursive(i, j + 1)
        s2 = self.minPathSumRecursive(i + 1, j)

        return self.grid[i][j] + min(s1, s2)

    def minPathSum(self, grid: List[List[int]]) -> int:
        self.grid = grid
        return self.minPathSumRecursive(0, 0)
