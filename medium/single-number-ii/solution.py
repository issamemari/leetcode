import numpy as np


class Solution:

    def singleNumber(self, nums: List[int]) -> int:
        bitCounts = np.zeros(32)

        for num in nums:
            for i in range(32):
                if num & (1 << i) != 0:
                    bitCounts[i] = (bitCounts[i] + 1) % 3

        res = 0
        for i in range(32):
            if bitCounts[i] > 0:
                res |= (1 << i)

        return np.int32(res)
