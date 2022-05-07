from typing import List


class Solution:

    def withinBounds(self, ij):
        i, j = ij
        return 0 <= i < self.m and 0 <= j < self.n

    def numIslands(self, grid: List[List[str]]) -> int:

        self.m, self.n = len(grid), len(grid[0])

        visited = set()

        count = 0
        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == "1" and (i, j) not in visited:
                    count += 1

                    queue = [(i, j)]

                    while len(queue) > 0:

                        current = queue.pop(0)
                        if current in visited:
                            continue

                        visited.add(current)

                        ci, cj = current
                        up = ci - 1, cj
                        down = ci + 1, cj
                        left = ci, cj - 1
                        right = ci, cj + 1

                        for d in [up, down, left, right]:
                            if self.withinBounds(d) and grid[d[0]][d[1]] == "1":
                                queue.append(d)

        return count
