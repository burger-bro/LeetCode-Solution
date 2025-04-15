from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def print_tree(node):
    if node is None:
        return
    print(node.val, end='')
    print_tree(node.left)
    print_tree(node.right)

def insert_node(cur_node: TreeNode, val: int):
    if cur_node is None:
        cur_node = TreeNode(val)
    else:
        if val > cur_node.val:
            cur_node.right = insert_node(cur_node.right, val)
        else:
            cur_node.left = insert_node(cur_node.left, val)
    return cur_node

def build_tree(array):
    root = None
    for a in array:
        root = insert_node(root, a)
    return root

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def traverse(node, max_v, min_v):
            if node is None:
                return True
            max_v = max(max_v, node.val)
            min_v = min(min_v, node.val)
            if node.left is not None and node.left.val >= min_v:
                return False
            if node.right is not None and node.right.val <= max_v:
                return False
            return traverse(node.left, max_v, min_v) and traverse(node.right, max_v, min_v)
        ans = traverse(root, root.val, root.val)
        print(ans)
        return ans
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        print("***************** start *****************")
        def traverse(node, flag):
            if node is None:
                return True, None, None
            # if node.left is None and node.right is None:
            #     return True, node.val, node.val
            
            ans1, l_min, l_max = traverse(node.left, 'l')
            ans2, r_min, r_max = traverse(node.right, 'r')
            print(node.val, l_max, r_min)
            tmp1, tmp2 = True, True
            if l_max is not None:
                tmp1 = l_max < node.val
            if r_min is not None:
                tmp2 = r_min > node.val
            p = [node.val]
            for v in [l_min, l_max, r_min, r_max]:
                if v is not None:
                    p.append(v)
            return ans1 and ans2 and tmp1 and tmp2, min(p), max(p)

        ans, _, _ = traverse(root, 'r')
        print(ans)
        return ans

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def traverse(node):
            if node is None:
                return True, None, None
            ans1, l_min, l_max = traverse(node.left)
            ans2, r_min, r_max = traverse(node.right)
            tmp1, tmp2 = True, True
            if l_max is not None:
                tmp1 = l_max < node.val
            if r_min is not None:
                tmp2 = r_min > node.val

            min_, max_ = node.val, node.val
            for v in [l_min, l_max, r_min, r_max]:
                if v is not None:
                    min_ = min(min_, v)
                    max_ = max(max_, v)
            return ans1 and ans2 and tmp1 and tmp2, min_, max_

        ans, _, _ = traverse(root)
        return ans

    # 自顶向下时，确定每一个值是否满足，用left_max和right_min两个变量进行维护
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def traverse(node, left_max, right_min):
            if node is None:
                return True
            
            ans1 = node.val < left_max and node.val > right_min
            ans2 = ans1 and traverse(node.left, node.val, right_min) and traverse(node.right, left_max, node.val)

            return ans2

        ans = traverse(root, float("inf"), -float("inf"))
        return ans
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def traverse(node, left_max, right_min):
            if node is None:
                return True
            ans = node.val < left_max and node.val > right_min and traverse(node.left, node.val, right_min) and traverse(node.right, left_max, node.val)
            return ans
        return traverse(root, float("inf"), -float("inf"))
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def traverse(node, max_v, min_v):
            if node is None:
                return True
            if node.left is not None and node.left.val >= min_v:
                return False
            if node.right is not None and node.right.val <= max_v:
                return False
            return traverse(node.left, max_v, min_v) and traverse(node.right, max_v, min_v)
        ans = traverse(root, root.val, root.val)
        print(ans)
        return ans



su = Solution()

# # case debug
# root = [120,70,140,50,100,130,160,20,55,75,110,119,135,150,200]
# root = build_tree(root)
# ans = True
# res = su.isValidBST(root)
# assert(res == ans)
# # exit(0)

# # case std 1
# root = [2,1,3]
# root = build_tree(root)
# ans = True
# res = su.isValidBST(root)
# assert(res == ans)

# # case std 2
# root = [5,1,4,3,6]
# root = build_tree(root)
# res = su.isValidBST(root)
# ans = True
# assert(res == ans)

# # case1 boundry
# root = [0]
# root = build_tree(root)
# res = su.isValidBST(root)
# ans = True
# assert(res == ans)
# # print_tree(root)

# # case2 category
# root = [0,1,2,3,4,5,6,7,8,9]
# root = build_tree(root)
# res = su.isValidBST(root)
# ans = True
# assert(res == ans)
# # print_tree(root)

# # case3 category
# root = [3,6,4,5]
# root = build_tree(root)
# res = su.isValidBST(root)
# ans = True
# assert(res == ans)
# # print_tree(root)

# # case4 category
# root = [2,2,2]
# root = build_tree(root)
# res = su.isValidBST(root)
# ans = False
# assert(res == ans)
# # print_tree(root)


s = [6,2,3,4,5,1,7]
# s = [1,7,3,4,5,6,2]

prev = None
start, end = None, None
for i in range(len(s)):
    if prev is not None and s[prev] > s[i]:
        if start is None:
            start = prev
        end = i
    prev = i

print(start, end)

