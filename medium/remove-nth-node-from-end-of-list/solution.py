from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        if self.next is None:
            return f"ListNode{{val: {self.val}, next: None}}"
        return f"ListNode{{val: {self.val}, next: {self.next.__repr__()}}}"



class Solution:

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        res =  head

        nodes = []

        current = head
        while current is not None:
            nodes.append(current)
            current = current.next

        nodes.append(None)

        if len(nodes) == 2:
            return None

        if n == 1:
            nodes[-n - 2].next = None
            return res

        if n == len(nodes):
            return res.next

        nodes[-n - 2].next = nodes[-n]

        return res




if __name__ == "__main__":
    s = Solution()
    head = ListNode(1)
    head.next = ListNode(2)
    print(s.removeNthFromEnd(head, 2))
