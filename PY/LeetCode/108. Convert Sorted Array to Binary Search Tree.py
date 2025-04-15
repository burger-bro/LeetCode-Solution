# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def dfs(left, right):
            if left == right:
                tmp = nums[right]
                return TreeNode(tmp)
            mid = (left + right) // 2
            l_tree = dfs(left, mid-1) if left != mid else None
            r_tree = dfs(mid+1, right)
            return TreeNode(nums[mid], l_tree, r_tree)
        return dfs(0, len(nums)-1)
