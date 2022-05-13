# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

    def __repr__(self):
        return f"{self.val}"


class Solution1:
    def connect(self, root: Node) -> Node:

        # The idea is to do depth first search (pre-order traversal)
        # while maintaining a list of nodes: the last visited node at
        # every level in the tree. During the traversal, for every new
        # node we encounter, we set the next pointer of the node in
        # the same level to point to the new node, then we set the new
        # node to be the last visited node in this level. Simple as
        # fuck.

        lastVisitedAtLevel = {}

        stack = [(root, 0)]

        while len(stack) > 0:
            node, level = stack.pop()

            if node is not None:
                if level in lastVisitedAtLevel:
                    lastVisitedAtLevel[level].next = node

                lastVisitedAtLevel[level] = node

                stack.append((node.left, level + 1))
                stack.append((node.right, level + 1))

        return root


class Solution2:
    def connect(self, root: 'Node') -> 'Node':
        queue = [(root, 0)]

        lastLevel = 0
        lastNodeInLevel = root
        while len(queue) > 0:
            node, level = queue.pop(0)

            if node is None:
                continue

            if level == lastLevel and lastNodeInLevel != node:
                lastNodeInLevel.next = node
            else:
                lastLevel = level

            lastNodeInLevel = node

            queue.append((node.left, level + 1))
            queue.append((node.right, level + 1))

        return root




if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(7)

    sol = Solution2()
    root = sol.connect(root)

    print(root)
