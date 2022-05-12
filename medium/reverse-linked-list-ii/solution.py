from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:

        if left == right:
            return head

        prev = None
        current = head
        next = current.next

        for _ in range(left - 1):
            prev = current
            current = next
            next = next.next

        current_tmp = current

        for _ in range(right - left):
            tmp = next.next
            next.next = current
            current = next
            next = tmp

        if prev is not None:
            prev.next = current
        else:
            head = current

        current_tmp.next = tmp

        return head
