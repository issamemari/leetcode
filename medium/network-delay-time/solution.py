import heapq

from collections import defaultdict
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        distances = {}

        queue = [(0, k)]

        adjacency = defaultdict(list)
        for u, v, w in times:
            adjacency[u].append((v, w))

        while queue:

            time, node = heapq.heappop(queue)

            if node in distances:
                continue

            distances[node] = time
            for neighbor, ntime in adjacency[node]:
                heapq.heappush(queue, (ntime + time, neighbor))

        if len(distances) == n:
            return max(distances.values())

        return -1
