from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack = []
        stack.append((p, q))
        while len(stack) > 0:
            current_p, current_q = stack.pop()
            if current_p is None and current_q is not None:
                return False
            if current_q is None and current_p is not None:
                return False
            if current_p is None and current_q is None:
                continue
            if current_p.val != current_q.val:
                return False
            stack.append((current_p.left, current_q.left))
            stack.append((current_p.right, current_q.right))
        return True
