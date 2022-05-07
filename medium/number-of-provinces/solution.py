from typing import List


class Solution:

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()
        count = 0
        for node in range(len(isConnected)):
            if node not in visited:
                count += 1
                queue = [node]
                while len(queue) > 0:
                    cur = queue.pop(0)
                    if cur in visited:
                        continue
                    visited.add(cur)
                    for j in range(len(isConnected[cur])):
                        if isConnected[cur][j] == 1:
                            queue.append(j)

        return count
