from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:

        res = 0
        lastLevel = 0

        queue = [(root, 0)]

        while queue:

            node, level = queue.pop(0)

            if node is None:
                continue

            if level > lastLevel:
                lastLevel = level
                res = 0

            res += node.val

            queue.append((node.left, level + 1))
            queue.append((node.right, level + 1))

        return res
