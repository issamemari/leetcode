from typing import List


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:

        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        for s in strs:

            countZeros = s.count("0")
            countOnes = len(s) - countZeros

            for i in range(m, countZeros - 1, -1):
                for j in range(n, countOnes - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i - countZeros][j - countOnes] + 1)

        return dp[m][n]
