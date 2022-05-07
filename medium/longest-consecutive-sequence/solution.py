from typing import List
from functools import lru_cache


class Solution:

    def longestConsecutive(self, nums: List[int]) -> int:

        nums = set(nums)

        @lru_cache(None)
        def longestSequenceEndingWithNum(num):
            if num not in nums:
                return 0
            return 1 + longestSequenceEndingWithNum(num - 1)

        res = 0
        for num in nums:
            res = max(res, longestSequenceEndingWithNum(num))

        return res
