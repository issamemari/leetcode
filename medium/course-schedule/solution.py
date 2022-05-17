from collections import defaultdict
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegzero = set(range(numCourses))
        adjacency = defaultdict(list)
        for pre in prerequisites:
            adjacency[pre[1]].append(pre[0])
            if pre[0] in indegzero:
                indegzero.remove(pre[0])

        if len(indegzero) == 0:
            return False

        visited = set()
        for course in indegzero:
            stack = [(course, [])]
            while stack:
                current, path = stack.pop()
                if current in visited:
                    continue

                visited.add(current)

                for dependentCourse in adjacency[current]:
                    if dependentCourse in path:
                        return False

                    stack.append((dependentCourse, path + [current]))

        return len(visited) == numCourses
