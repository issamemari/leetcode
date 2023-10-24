from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        level_to_max_value = []
        stack = [(root, 0)]
        while stack:
            current_node, current_level = stack.pop()
            if current_level >= len(level_to_max_value):
                level_to_max_value.append(current_node.val)
            else:
                level_to_max_value[current_level] = max(level_to_max_value[current_level], current_node.val)

            if current_node.left is not None:
                stack.append((current_node.left, current_level + 1))

            if current_node.right is not None:
                stack.append((current_node.right, current_level + 1))

        return level_to_max_value
