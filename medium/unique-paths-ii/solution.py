from typing import List


class Solution:

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
