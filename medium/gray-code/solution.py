import numpy as np

from typing import List


class Solution:

    def grayCode(self, n: int) -> List[int]:

        res = []
        for i in range(2 ** n):

            num = 0
            for j in range(n):
                rem = (i % 2 ** (j + 2)) // 2 ** j

                num *= 2
                if rem != 0 and rem != 3:
                    num += 1

            res.append(num)

        return res
