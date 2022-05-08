from collections import defaultdict
from typing import List


class Solution:

    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:

        n = len(img1)

        img1ones = []
        img2ones = []
        for i in range(n):
            for j in range(n):
                if img1[i][j] == 1:
                    img1ones.append((i, j))
                if img2[i][j] == 1:
                    img2ones.append((i, j))


        translationCounts = defaultdict(int)
        for t1 in img1ones:
            for t2 in img2ones:
                translation = t2[0] - t1[0], t2[1] - t1[1]
                translationCounts[translation] += 1

        if len(translationCounts) == 0:
            return 0

        return max(translationCounts.values())
