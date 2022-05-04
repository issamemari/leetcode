from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        done = set()
        for i in range(n):
            for j in range(n):
                if (i, j) in done:
                    continue

                current = matrix[i][j]
                matrix[i][j] = None

                ip, jp = j, n - i - 1
                while matrix[ip][jp] != None:

                    new_current = matrix[ip][jp]
                    matrix[ip][jp] = current
                    current = new_current

                    done.add((ip, jp))

                    ip, jp = jp, n - ip - 1

                matrix[ip][jp] = current
                done.add((ip, jp))
