# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse(s: ListNode):
    prev = None
    current = s
    next = s.next

    while next is not None:
        current.next = prev
        prev = current
        current = next
        next = current.next

    current.next = prev
    return current


class Solution:

    def addRecursive(self, l1, l2, carry, result_current):
        v1 = 0
        if l1:
            v1 = l1.val

        v2 = 0
        if l2:
            v2 = l2.val

        v = v1 + v2 + carry
        carry = v // 10
        v = v % 10

        result_current.val = v

        new_l1 = None
        if l1:
            new_l1 = l1.next

        new_l2 = None
        if l2:
            new_l2 = l2.next

        if new_l1 is not None or new_l2 is not None or carry > 0:
            result_current.next = ListNode()
            result_current = result_current.next
            self.addRecursive(new_l1, new_l2, carry, result_current)

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result_head = ListNode(val=-1, next=None)
        result_head.next = ListNode(val=-1, next=None)
        self.addRecursive(l1, l2, 0, result_head.next)
        return result_head.next
