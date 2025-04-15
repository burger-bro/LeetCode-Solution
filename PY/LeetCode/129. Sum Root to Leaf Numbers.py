from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans_sum = 0
        def dfs(root, cur_val=0):
            nxt_val = cur_val * 10 + root.val
            # print(root.val, cur_val)
            if root.left is None and root.right is None:
                return nxt_val
            left_val = 0 if root.left is None else dfs(root.left, nxt_val)
            right_val = 0 if root.right is None else dfs(root.right, nxt_val)
            # print(left_val, right_val)
            return left_val + right_val

        ans_sum = dfs(root)
        return ans_sum

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans_sum = 0
        def dfs(root, cur_val=0):
            nxt_val = cur_val * 10 + root.val
            left_val = 0 if root.left is None else dfs(root.left, nxt_val)
            right_val = 0 if root.right is None else dfs(root.right, nxt_val)
            return max(left_val + right_val, nxt_val)

        ans_sum = dfs(root)
        return ans_sum

su = Solution()
root = TreeNode(1, left=TreeNode(2), right=TreeNode(3))
print(su.sumNumbers(root))

root = TreeNode(1)
print(su.sumNumbers(root))

root = TreeNode(1, left=TreeNode(2))
print(su.sumNumbers(root))
