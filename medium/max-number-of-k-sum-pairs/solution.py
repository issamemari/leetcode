from collections import Counter
from typing import List


class Solution:

    def maxOperations(self, nums: List[int], k: int) -> int:

        counter = Counter(nums)
        deleted = set()

        res = 0
        for i in range(len(nums)):

            if i in deleted:
                continue

            diff = k - nums[i]
            if diff in deleted:
                continue

            if diff in counter:
                count1 = counter[diff]
                count2 = counter[nums[i]]

                if diff != nums[i]:
                    res += min(count1, count2)
                    deleted.add(nums[i])
                else:
                    res += count1 // 2

                deleted.add(diff)

        return res
