from typing import List


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        n = len(grid)
        if grid[0][0] or grid[n - 1][n - 1]:
            return -1

        queue, visited = [((0, 0), 1)], set()

        neighbors = [
            (1, 1),
            (0, 1),
            (1, 0),
            (1, -1),
            (-1, 1),
            (-1, 0),
            (0, -1),
            (-1, -1),
        ]

        while queue:

            (i, j), length = queue.pop(0)

            if (i, j) in visited:
                continue

            visited.add((i, j))

            if (i, j) == (n - 1, n - 1):
                return length

            for k, l in neighbors:
                if 0 <= i + k < n and 0 <= j + l < n and grid[i + k][j + l] == 0:
                    queue.append(((i + k, j + l), length + 1))

        return -1
