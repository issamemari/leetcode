from typing import List


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:

        if len(graph) <= 1:
            return True

        # Loop through nodes. For every node, assert that the graph is Bipartite
        # From one node, we do BFS while keeping track of the distance in number
        # of edges from the source node. Nodes that have odd distance are assumed to be
        # in the other set of nodes. Nodes that have even distance are assumed to be in
        # the same set. If at any point during the BFS, we find a node with odd distance
        # that belongs to the even set, we return False

        IS_ODD = True
        IS_EVEN = False

        visited = set()
        for source in range(len(graph)):

            if source in visited:
                continue

            visited.add(source)


            evenSet = set()
            oddSet = set()

            queue = []
            for j in graph[source]:
                oddSet.add(j)
                queue.append((j, IS_ODD))

            while len(queue) > 0:
                current, oddity = queue[0]
                queue = queue[1:]

                if current in visited:
                    continue

                visited.add(current)

                for k in graph[current]:
                    if oddity == IS_ODD and k in oddSet:
                        return False
                    if oddity == IS_EVEN and k in evenSet:
                        return False

                    if oddity == IS_ODD:
                        evenSet.add(k)
                        queue.append((k, IS_EVEN))
                    else:
                        oddSet.add(k)
                        queue.append((k, IS_ODD))

        return True


if __name__ == "__main__":
    s = Solution()
    print(s.isBipartite([[1, 3], [0, 2], [1, 3], [0, 2]]))
