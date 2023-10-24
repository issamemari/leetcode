from typing import List


class Solution:
    def __init__(self):
        self.memory = {}

    def numSquares(self, n: int) -> int:
        if n in self.memory:
            return self.memory[n]

        minimum_count = 10000
        for i in range(int(n ** 0.5), 0, -1):
            candidate = i ** 2
            if candidate == n:
                self.memory[n] = 1
                return 1

            current_count = 1 + self.numSquares(n - candidate)
            if current_count < minimum_count:
                minimum_count = current_count

        self.memory[n] = minimum_count
        return minimum_count
