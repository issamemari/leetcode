from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        if self.next is None:
            return f"ListNode{{val: {self.val}, next: None}}"
        return f"ListNode{{val: {self.val}, next: {self.next.__repr__()}}}"


class Solution:

    def sortingFunction(self, x):
        if x is not None:
            return x.val
        return 2 ** 31

    def resort(self, lists):
        if lists[0] == None:
            return lists[1:]

        new_lists = []
        for l in lists:
            if l is not None:
                new_lists.append(l)

        return sorted(new_lists, key=self.sortingFunction)

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        result_head = ListNode(val=None, next=None)
        result = result_head

        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]

        sorted_lists = sorted(lists, key=self.sortingFunction)

        while sorted_lists[0] is not None and len(sorted_lists) > 1:
            while (
                sorted_lists[0] is not None
                and sorted_lists[1] is not None
                and len(sorted_lists) > 1
                and sorted_lists[0].val <= sorted_lists[1].val
            ):
                result.val = sorted_lists[0].val
                result.next = ListNode(val=None, next=None)
                result = result.next
                sorted_lists[0] = sorted_lists[0].next

            sorted_lists = self.resort(sorted_lists)

        if sorted_lists[0] is not None:
            result.val = sorted_lists[0].val
            result.next = sorted_lists[0].next

        if result_head.val is None:
            return None

        return result_head


if __name__ == "__main__":
    s = Solution()

    # example with one empty list and another list containing only 1
    print(s.mergeKLists([None, ListNode(val=1, next=None)]))
