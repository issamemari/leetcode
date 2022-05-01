from typing import List

from collections import Counter


class Solution:

    def deleteAndEarn(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        numsSet = sorted(set(nums))

        counts = Counter(nums)

        fib0 = None
        fib1 = None
        for num in numsSet:
            if (num - 1) not in numsSet:
                t = 0
                if fib1 is not None:
                    t = fib1
                t += counts[num] * num
                fib0 = fib1
                fib1 = t
                continue

            t1 = 0
            if fib0 is not None:
                t1 += fib0
            t1 += counts[num] * num
            t2 = fib1

            fib0 = fib1
            fib1 = max(t1, t2)

        return fib1
