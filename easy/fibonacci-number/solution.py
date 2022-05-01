class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n

        fibs = [0, 1]
        for i in range(2, n + 1):
            fibs.append(fibs[i - 1] + fibs[i - 2])

        return fibs[-1]
