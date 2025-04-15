from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        global_node = None
        def dfs(node):
            nonlocal global_node
            node.right is not None and dfs(node.right)
            node.left is not None and dfs(node.left)
            node.right = global_node
            global_node = node
        dfs(root)
        return global_node


