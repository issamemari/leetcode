from typing import List


class Solution:

    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        for i in range(2 ** len(nums)):
            subset = []

            count = 0

            subsetIndex = i
            while subsetIndex != 0:
                rem = subsetIndex % 2
                subsetIndex = subsetIndex // 2

                if rem == 1:
                    subset.append(nums[count])

                count += 1

            res.append(subset)

        return res
