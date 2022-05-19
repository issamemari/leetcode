from typing import Tuple, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def isFull(self, root: TreeNode) -> Tuple[int, bool]:
        depth = 0

        current = root
        while current is not None:
            current = current.left
            depth += 1

        depthRight = 0
        current = root
        while current is not None:
            current = current.right
            depthRight += 1

        return depth, depth == depthRight

    def countNodes(self, root: Optional[TreeNode]) -> int:

        if root is None:
            return 0

        depth, isFull = self.isFull(root)

        if isFull:
            return 2 ** depth - 1

        countLeft = self.countNodes(root.left)
        countRight = self.countNodes(root.right)

        return 1 + countLeft + countRight
