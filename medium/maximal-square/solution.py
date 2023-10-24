from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 0:
            return 0

        if len(matrix[0]) == 0:
            return 0

        n_rows = len(matrix)
        n_cols = len(matrix[0])

        for row in range(n_rows):
            for col in range(n_cols):
                matrix[row][col] = int(matrix[row][col])

        mem = {}
        for row in range(n_rows):
            mem[(row, 0)] = matrix[row][0]

        for col in range(n_cols):
            mem[(0, col)] = matrix[0][col]

        for row in range(1, n_rows):
            for col in range(1, n_cols):
                if matrix[row][col] != 1:
                    mem[(row, col)] = 0
                    continue

                top = mem[(row - 1, col)]
                left = mem[(row, col - 1)]
                diag = mem[(row - 1, col - 1)]

                if top == 0 or left == 0 or diag == 0:
                    mem[(row, col)] = 1
                    continue

                if top == left and top <= diag:
                    mem[(row, col)] = top + 1
                    continue

                if top == left and top > diag:
                    mem[(row, col)] = top
                    continue

                mem[(row, col)] = min(top, left) + 1

        return max(mem.values()) ** 2
