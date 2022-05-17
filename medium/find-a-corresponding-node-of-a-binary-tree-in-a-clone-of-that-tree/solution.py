class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def getTargetCopy(
        self, original: TreeNode, cloned: TreeNode, target: TreeNode
    ) -> TreeNode:
        queue = [(original, cloned)]

        visited = set()

        while queue:

            current_original, current_cloned = queue.pop(0)

            if current_original is None or current_original.val in visited:
                continue

            visited.add(current_original.val)

            if current_original == target:
                return current_cloned

            queue.append((current_original.left, current_cloned.left))
            queue.append((current_original.right, current_cloned.right))
