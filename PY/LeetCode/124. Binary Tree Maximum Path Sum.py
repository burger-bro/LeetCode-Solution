from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        print("************start************")
        ret = -float("inf")
        def dfs(node):
            nonlocal ret
            if node.left is None and node.right is None:
                ret = max(ret, node.val)
                return node.val
            l_max_sum = dfs(node.left) if node.left is not None else -float("inf")
            r_max_sum = dfs(node.right) if node.right is not None else -float("inf")
            print(l_max_sum, r_max_sum)
            # cur_max = node.val+max(l_max_sum,r_max_sum)
            cur_max = max(node.val, node.val+max(l_max_sum,r_max_sum))
            ret = max(ret, cur_max)
            ret = max(ret, node.val+l_max_sum+r_max_sum)
            return cur_max
        dfs(root)
        print("ret:", ret)
        return ret

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        print("************start************")
        ret = -float("inf")
        def dfs(node):
            nonlocal ret
            if node is None: return -float("inf")
            if node.left is None and node.right is None:
                ret = max(ret, node.val)
                return node.val
            l_sum, r_sum = dfs(node.left), dfs(node.right)
            cur_max = max(node.val, node.val+max(l_sum, r_sum))
            ret = max([ret, node.val, cur_max, node.val+l_sum+r_sum])
            return cur_max
        dfs(root)
        print("ret:", ret)
        return ret

def build_tree(array):
    def build(i):
        if i-1>len(array)-1 or array[i-1] is None: return
        node = TreeNode(array[i-1])
        node.left = build(2*i)
        node.right = build(2*i+1)
        return node
    return build(1)
    
def print_tree(node):
    if node is None:
        return
    print(node.val, end=' ')
    print_tree(node.left)
    print_tree(node.right)

su = Solution()

# case std1
root = [1,2,3]
root = build_tree(root)
# print_tree(root)
res = su.maxPathSum(root)
ans = 6
assert(res == ans)

# case std2
root = [-10,9,20,None,None,15,7]
root = build_tree(root)
# print_tree(root)
res = su.maxPathSum(root)
ans = 42
assert(res == ans)

# case1 min
root = [1]
root = build_tree(root)
# print_tree(root)
res = su.maxPathSum(root)
ans = 1
assert(res == ans)

# case2 min
root = [-20]
root = build_tree(root)
# print_tree(root)
res = su.maxPathSum(root)
ans = -20
assert(res == ans)

# case3 min
root = [-20, 2]
root = build_tree(root)
# print_tree(root)
res = su.maxPathSum(root)
ans = 2
assert(res == ans)

# case4 min
root = [-20, 2, None, 5]
root = build_tree(root)
# print_tree(root)
res = su.maxPathSum(root)
ans = 7
assert(res == ans)

# case5 
root = [-20, 2, None, 5, None, None, None, -10]
root = build_tree(root)
# print_tree(root)
res = su.maxPathSum(root)
ans = 7
assert(res == ans)

# case6
root = [1, 2, None, -37, None, None, None, -10]
root = build_tree(root)
# print_tree(root)
res = su.maxPathSum(root)
ans = 3
assert(res == ans)

# case6
root = [-37, -21, None, -37, None, None, None, -999]
root = build_tree(root)
# print_tree(root)
res = su.maxPathSum(root)
ans = -21
assert(res == ans)

# case7 perf

root = [i for i in range(30000)]
root = build_tree(root)
# print_tree(root)
res = su.maxPathSum(root)
ans = -21
# assert(res == ans)
