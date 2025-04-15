from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        minimum = float("inf")

    def minDepth(self, root: Optional[TreeNode]) -> int:
        queue = deque([[root, 1]]) 
        while queue:
            cur_node, depth = queue.popleft()
            if cur_node.left is None and cur_node.right is None:
                return depth
            if cur_node.left is not None:
                queue.append([cur_node.left, depth+1])
            if cur_node.right is not None:
                queue.append([cur_node.right, depth+1])