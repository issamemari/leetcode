class Solution:

    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0

        if n <= 2:
            return 1

        fibs = [0, 1, 1]

        for i in range(3, n + 1):
            fibs.append(fibs[i - 1] + fibs[i - 2] + fibs[i - 3])

        return fibs[-1]
