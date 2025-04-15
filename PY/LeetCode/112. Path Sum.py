from typing import Optional
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def helper(node, targetSum):
            if node is None: return False
            if node.left is None and node.right is None:
                return targetSum - node.val == 0
            next_target = targetSum-node.val
            return helper(node.left, next_target) or helper(node.right, next_target)
        return helper(root, targetSum)
    
#   X:12345 q:(1,4,5,2) p:(3,4,1)*(2,5)
#  pX:35412
# qpX:32541       
# qpX:3 5 1
#  qp:1,3,5

#   X:12345
#  qX:41352
# pqX:13425
# pqX: 342
#  pq:2,3,4
