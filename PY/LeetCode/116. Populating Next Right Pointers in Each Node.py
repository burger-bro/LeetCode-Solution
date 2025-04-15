from typing import Optional
from collections import deque
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        queue = deque([root])
        while queue:
            length = len(queue)
            prev = None
            while length:
                length -= 1
                node = queue.popleft()
                if prev is not None:
                    prev.next = node
                node.left is not None and queue.append(node.left)
                node.right is not None and queue.append(node.right)
        return root
            
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        start = root
        while start is not None:
            cur = start

            while cur is not None:
                cur.left is not None and cur.left.next = cur.right
                cur.right is not None and cur.next is not None and cur.right.next = cur.next.left
                cur = cur.next
        return root
