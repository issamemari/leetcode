from typing import List


class Solution1:

    def __init__(self):
        self.memory = {}

    def helper(self, row, column, obstacleGrid) -> int:
        if (row, column) in self.memory:
            return self.memory[(row, column)]

        m, n = len(obstacleGrid), len(obstacleGrid[0])

        if obstacleGrid[row][column] == 1:
            self.memory[(row, column)] = 0
            return 0

        if row == m - 1 and column == n - 1:
            self.memory[(row, column)] = 1
            return 1

        count = 0
        if row < m - 1 and obstacleGrid[row + 1][column] != 1:
            count += self.helper(row + 1, column, obstacleGrid)

        if column < n - 1 and obstacleGrid[row][column + 1] != 1:
            count += self.helper(row, column + 1, obstacleGrid)

        self.memory[(row, column)] = count
        return count

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        return self.helper(0, 0, obstacleGrid)


class Solution2:

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])

        countGrid = [
            [0 for _ in range(n)]
            for _ in range(m)
        ]

        queue = [(m - 1, n - 1)]
        visited = set()
        while len(queue) > 0:
            row, col = queue.pop(0)

            if (row, col) in visited:
                continue
            
            visited.add((row, col))

            if obstacleGrid[row][col] != 1:
                if row == m - 1 and col == n - 1:
                    countGrid[row][col] = 1

                if row < m - 1:
                    countGrid[row][col] += countGrid[row + 1][col]

                if col < n - 1:
                    countGrid[row][col] += countGrid[row][col + 1]

            if row > 0:
                queue.append((row - 1, col))

            if col > 0:
                queue.append((row, col - 1))

        return countGrid[0][0]
