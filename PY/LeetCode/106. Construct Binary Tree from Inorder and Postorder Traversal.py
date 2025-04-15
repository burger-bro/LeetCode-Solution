from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        inorder_dict = {v:i for i, v in enumerate(inorder)}
        def helper(_in, _post):
            if not _in: return None
            root_val = _post[-1]
            idx = _in.index(root_val)
            left_in = _in[:idx]
            right_in = _in[idx+1:]

            left_post = _post[:idx]
            right_post = _post[idx:-1]            
            left_trees = helper(left_in, left_post)
            right_trees = helper(right_in, right_post)
            return TreeNode(root_val, left_trees, right_trees)
        return helper(inorder, postorder)

# a = [1,3,4,5,6,7]
# print(a.index(6))

su = Solution()
inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
su.buildTree(inorder, postorder)


