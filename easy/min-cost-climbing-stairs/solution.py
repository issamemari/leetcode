class Solution:

    def minCostClimbingStairs(self, cost: List[int]) -> int:

        if len(cost) <= 1:
            return 0

        fibs0 = 0
        fibs1 = min(cost[-2], cost[-1])

        for i in reversed(range(len(cost) - 2)):
            t1 = cost[i] + fibs1
            t2 = cost[i + 1] + fibs0

            fibs0 = fibs1
            fibs1 = min(t1, t2)

        return fibs1
