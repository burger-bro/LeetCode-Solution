from typing import Optional
from functools import reduce
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        max_depth = 0
        deepest_nodes = []
        lca = root
        def dfs(node, parents, depth):
            nonlocal max_depth, deepest_nodes, lca
            if node.left is None and node.right is None:
                if depth > max_depth:
                    deepest_nodes.clear()
                    max_depth = depth
                    deepest_nodes.append(node)
                    lca = parents
                elif depth == max_depth:
                    deepest_nodes.append(node)
            node.left is not None and dfs(node.left, node, depth+1)
            node.right is not None and dfs(node.right, node, depth+1)
            return
        dfs(root, root, 0)
        return lca if len(deepest_nodes)==2 else deepest_nodes[0]

    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        max_depth = 0
        deepest_path = []
        def dfs(node, path):
            nonlocal max_depth
            path.append(node)
            if node.left is None and node.right is None:
                if len(path) > max_depth:
                    max_depth = len(path)
                    deepest_path.clear()
                    deepest_path.append(path.copy())
                elif len(path) == max_depth:
                    deepest_path.append(path.copy())
            node.left is not None and dfs(node.left, path) #尝试不pop
            node.right is not None and dfs(node.right, path)
            path.pop()
            return
        dfs(root, [])
        print("len", len(deepest_path))
        print("path len", len(deepest_path[0]))
        for path in deepest_path:
            print("begin")
            for node in path:
                print(id(node))
            print("eng")
        if len(deepest_path) == 1: return deepest_path[0][-1]
        for i in range(len(deepest_path[0])-1, -1, -1):
            for path in deepest_path[1:]:
                if deepest_path[0][i] is not path[i]:
                    break
                return deepest_path[0][i]


    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        max_depth = 0
        deepest_path = []
        def dfs(node, path):
            nonlocal max_depth
            path.append(node)
            if node.left is None and node.right is None:
                if len(path) > max_depth:
                    max_depth = len(path)
                    deepest_path.clear()
                    deepest_path.append(path.copy())
                elif len(path) == max_depth:
                    deepest_path.append(path.copy())
            node.left is not None and dfs(node.left, path) #尝试不pop
            node.right is not None and dfs(node.right, path)
            path.pop()
            return
        dfs(root, [])
        if len(deepest_path) == 1: return deepest_path[0][-1]
        for i in range(len(deepest_path[0])-1, -1, -1):
            for path in deepest_path[1:]:
                if deepest_path[0][i] is not path[i]:
                    break
            else:
                return deepest_path[0][i]


    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        max_depth = 0
        lca = root
        def dfs(node, depth):
            nonlocal max_depth, lca
            if node.left is None and node.right is None:
                if depth > max_depth:
                    max_depth = depth
                    lca = node
                return 1
            cur_cnt, left_cnt, right_cnt = 0, 0, 0 
            if node.left is not None:
                left_cnt = max(cur_cnt, dfs(node.left, depth+1))
            if node.right is not None:
                right_cnt = max(cur_cnt, dfs(node.right, depth+1))
            # print(max_depth, cur_cnt, left_cnt, right_cnt)
            cur_cnt = max(left_cnt, right_cnt)
            if max_depth-cur_cnt==depth and left_cnt==right_cnt:
                lca = node
            return cur_cnt+1
        dfs(root, 0)
        return lca

    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node, depth):
            if node.left is None and node.right is None:
                return 1, node
            left_cnt, right_cnt = 0, 0 
            left_node, right_node = None, None
            if node.left is not None:
                left_cnt, left_node = dfs(node.left, depth+1)
            if node.right is not None:
                right_cnt, right_node = dfs(node.right, depth+1)
            # print(max_depth, cur_cnt, left_cnt, right_cnt)
            if left_cnt==right_cnt:
                return left_cnt+1, node
            return (left_cnt+1, left_node) if left_cnt > right_cnt else (right_cnt+1, right_node)
        _, lca = dfs(root, 0)
        return lca

    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node, depth):
            if node.left is None and node.right is None:
                return depth, node
            left_cnt, right_cnt = 0, 0 
            left_node, right_node = None, None
            if node.left is not None:
                left_cnt, left_node = dfs(node.left, depth+1)
            if node.right is not None:
                right_cnt, right_node = dfs(node.right, depth+1)
            # print(max_depth, cur_cnt, left_cnt, right_cnt)
            if left_cnt==right_cnt:
                return depth, node
            return (left_cnt, left_node) if left_cnt > right_cnt else (right_cnt, right_node)
        _, lca = dfs(root, 0)
        return lca

A = "XXX"
B = "YYY"
print(id(A), id(B))
a = [[2,A], [4, A], [6,A]]

i = 1

x = reduce(lambda a, b: a is b, [l[i] for l in a])
print(x)
