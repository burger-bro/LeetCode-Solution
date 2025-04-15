from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        ans = True
        def traverse(node):
            nonlocal ans
            if node is None:
                return 0
            left_depth = traverse(node.left)
            right_depth = traverse(node.right)
            if abs(left_depth - right_depth) > 1:
                ans = False
            return max(left_depth, right_depth) + 1
        traverse(root)
        return ans