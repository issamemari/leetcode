from dataclasses import dataclass
from collections import defaultdict
from typing import Optional, List


@dataclass
class Node:
    index: int
    parent: Optional


class Solution:
    def getEdge(self, index1, index2):
        if index1 < index2:
            return index1, index2
        return index2, index1

    def findAncestors(self, node: Node):
        ancestors = []
        ptr = node
        while ptr.parent is not None:
            ptr = ptr.parent
            ancestors.append(ptr)
        return ancestors

    def findEdges(self, node: Node, ancestor: Node):
        edges = []
        ptr = node
        while ptr.parent is not None and ptr.parent.index != ancestor.index:
            edges.append(self.getEdge(ptr.index, ptr.parent.index))
            ptr = ptr.parent

        if ptr.parent is not None and ptr.parent.index == ancestor.index:
            edges.append(self.getEdge(ptr.index, ptr.parent.index))

        return edges

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        edges_to_remove = set()

        adjacencyDict = defaultdict(list)
        for edge in edges:
            adjacencyDict[edge[0]].append(edge[1])
            adjacencyDict[edge[1]].append(edge[0])

        visited = {}

        # we can start from any node
        queue = [Node(index=edges[0][0], parent=None)]

        while len(queue) > 0:

            current = queue.pop(0)

            if current.index in visited:
                # here is the meat of the algo
                # here, it means we just popped a node that has been visited before
                # a node can only be visited before if there are two routes that lead
                # two it from the starting node
                # now we should list all the ancestors of this interesting node.
                # and also list all the ancestors of the parent node
                current_ancestors = self.findAncestors(current)
                other_ancestors = [visited[current.index]] + self.findAncestors(
                    visited[current.index]
                )

                # find the lowest common ancestor
                i = 1
                while (
                    i < min(len(current_ancestors), len(other_ancestors))
                    and current_ancestors[-i].index == other_ancestors[-i].index
                ):
                    i += 1

                if not current_ancestors[-i].index == other_ancestors[-i].index:
                    i -= 1

                lowest_common_ancestor = current_ancestors[-i]

                # all edges between current and lowest common ancestor can be removed
                # all edges between neighbor and lowest common ancestor can be removed
                # edge between current and neighbor can be removed
                edges_to_remove.add(
                    self.getEdge(current.index, visited[current.index].index)
                )

                edges_to_remove.update(self.findEdges(current, lowest_common_ancestor))
                edges_to_remove.update(
                    self.findEdges(visited[current.index], lowest_common_ancestor)
                )

                for edge in reversed(edges):
                    if tuple(edge) in edges_to_remove:
                        return edge

            visited[current.index] = current.parent

            for neighbor in adjacencyDict[current.index]:
                if neighbor != current.parent:
                    if neighbor not in visited:
                        queue.append(Node(index=neighbor, parent=current))


if __name__ == "__main__":
    solution = Solution()
    edges = [
        [16, 25],
        [7, 9],
        [3, 24],
        [10, 20],
        [15, 24],
        [2, 8],
        [19, 21],
        [2, 15],
        [13, 20],
        [5, 21],
        [7, 11],
        [6, 23],
        [7, 16],
        [1, 8],
        [17, 20],
        [4, 19],
        [11, 22],
        [5, 11],
        [1, 16],
        [14, 20],
        [1, 4],
        [22, 23],
        [12, 20],
        [15, 18],
        [12, 16],
    ]
    print(solution.findRedundantConnection(edges))
