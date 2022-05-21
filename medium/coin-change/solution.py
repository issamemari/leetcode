from typing import List


class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:

        visited = set()
        queue = [(0, 0)]

        while queue:

            currentAmount, coinCount = queue.pop(0)

            if currentAmount == amount:
                return coinCount

            if currentAmount in visited:
                continue

            visited.add(currentAmount)

            for coin in coins:
                if coin + currentAmount <= amount:
                    queue.append((coin + currentAmount, coinCount + 1))

        return -1
