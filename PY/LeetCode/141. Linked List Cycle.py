from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        node_dict = set()
        p = head
        while p:
            if p not in node_dict:
                node_dict.add(p)
            else:
                return True
            p = p.next
        return False

    def hasCycle(self, head: Optional[ListNode]) -> bool:
        p1, p2 = head, head
        while True:
            if p1.next is None:
                return False
            if p2.next is None or p2.next.next is None:
                return False

            p1 = p1.next
            p2 = p2.next.next
            if p1 == p2:
                return True

