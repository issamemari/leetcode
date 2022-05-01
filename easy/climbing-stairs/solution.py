class Solution:

    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        fibs = [1, 2]

        for i in range(2, n):
            fibs.append(fibs[i - 1] + fibs[i - 2])

        return fibs[-1]
