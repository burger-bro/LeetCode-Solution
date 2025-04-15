
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        start = root
        while start is not None:
            cur = start
            first_left_node = None
            prev = None
            while cur is not None:
                if cur.left is not None:
                    if prev is not None:
                        prev.next = cur.left
                    prev = cur.left
                    if first_left_node is None:
                        first_left_node = cur.left
                if cur.right is not None:
                    if prev is not None:
                        prev.next = cur.right
                    prev = cur.right
                    if first_left_node is None:
                        first_left_node = cur.right
                cur = cur.next
            start = first_left_node
        return root

    def connect(self, root: 'Node') -> 'Node':
        start = root
        while start is not None:
            cur = start
            first_left_node = Node(0)
            prev = first_left_node
            while cur is not None:
                if cur.left is not None:
                    prev.next = cur.left
                    prev = cur.left
                if cur.right is not None:
                    prev.next = cur.right
                    prev = cur.right
                cur = cur.next
            start = first_left_node.next
        return root    



