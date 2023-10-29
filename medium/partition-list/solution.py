from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def insert(self, val: int, head: ListNode, threshold: int) -> ListNode:
        current = head
        prev = None

        while current is not None and current.val < threshold:
            prev = current
            current = current.next

        if current is None:
            return head

        if prev is None:
            return ListNode(val, next=head)

        prev.next = ListNode(val, next=current)

        return head

    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if head is None:
            return None

        current = head
        while current and current.val < x:
            current = current.next

        if current is None:
            return head

        next = current.next

        while next is not None:
            if next.val < x:
                head = self.insert(next.val, head, x)
                current.next = next.next
                next = next.next
            else:
                current = next
                next = next.next

        return head
