from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        if self.next is None:
            return f"ListNode{{val: {self.val}, next: None}}"
        return f"ListNode{{val: {self.val}, next: {self.next.__repr__()}}}"


class Solution:

    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head is None:
            return None

        if head.next is None:
            return head

        res = head.next

        prev = None
        current = head
        next = head.next

        while next is not None:
            current.next = next.next
            next.next = current

            if prev is not None:
                prev.next = next

            if current.next is None:
                break

            prev = current
            current = current.next
            next = current.next

        return res
