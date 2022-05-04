from typing import List


class Solution:

    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        for i in range(1, numRows):
            row = [1]
            for j in range(len(res[i - 1]) - 1):
                row.append(res[i - 1][j] + res[i - 1][j + 1])
            row.append(1)
            res.append(row)
        return res
