from typing import List


class Solution:

    def minimumTotal(self, triangle: List[List[int]]) -> int:

        for i in range(1, len(triangle)):
            for j in range(i + 1):

                n1, n2 = None, None
                if j > 0:
                    n1 = triangle[i - 1][j - 1]
                if j < i:
                    n2 = triangle[i - 1][j]

                if n1 is not None and n2 is not None:
                    m = min(n1, n2)
                elif n1 is not None:
                    m = n1
                else:
                    m = n2

                triangle[i][j] += m

        return min(triangle[-1])
