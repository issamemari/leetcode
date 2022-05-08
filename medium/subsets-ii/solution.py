from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = set()
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

            res.add(tuple(sorted(subset)))

        r = []
        for x in res:
            r.append(list(x))
        return r
