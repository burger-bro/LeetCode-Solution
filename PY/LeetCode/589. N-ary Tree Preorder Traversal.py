from typing import List, Optional
from collections import deque
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children


class Solution:
    def preorder1(self, root: 'Node') -> List[int]:
        ans = []
        if root is None: return ans
        def travserse(node: Node):
            nonlocal ans
            ans.append(node.val)
            if node.children is not None:
                for child in node.children:
                    travserse(child)
        travserse(root)
        return ans

    def preorder(self, root: 'Node') -> List[int]:
        ans = []
        if root is None: return ans
        queue = deque([root])
        while queue:
            node: Node = queue.popleft()
            ans.append(node.val)
            if node.children is not None:
                queue.extendleft(node.children[::-1])
        print(ans)
        return ans

root = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
node3.children = [node5, node6]
root.children = [node3, node2, node4]
su = Solution()
su.preorder(root)

root = Node()

su.preorder(None)