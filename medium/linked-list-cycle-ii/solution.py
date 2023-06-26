from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        seen = set([head])
        current_node = head
        while current_node.next is not None:
            current_node = current_node.next
            if current_node in seen:
                return current_node

            seen.add(current_node)

        return None

if __name__ == "__main__":
    sol = Solution()
    head = ListNode(3)
    head.next = ListNode(2)
    head.next.next = ListNode(0)
    head.next.next.next = ListNode(-4)
    head.next.next.next.next = head.next
    print(sol.detectCycle(head))
