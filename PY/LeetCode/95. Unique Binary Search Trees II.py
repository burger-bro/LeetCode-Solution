from typing import List, Optional
from itertools import permutations
from functools import cache

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
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        per = permutations(list(range(1, n+1)))
        # print(list(per))
        tree_list = []
        for p in per:
            tree_list.append(build_tree(p))

        # print(tree_list)
        # for i, p in enumerate(tree_list):
        #     print(i, "*********")
        #     print_tree(p)
        #     print("")
        
        ans_list = [tree_list[0]]
        def check(tree_a, tree_b):
            flag = True
            if tree_a is not None and tree_b is not None:
                if tree_a.val != tree_b.val:
                    flag = False
                else:
                    flag = check(tree_a.left, tree_b.left) and check(tree_a.right, tree_b.right)
            else:
                flag = False
            return flag
        
        for tree in tree_list[1:]:
            for t in ans_list:
                if check(t, tree):
                    continue
                ans_list.append(tree)
        return ans_list

    # 自顶向下的动态规划，使用cache
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        @cache
        def dfs(left, right):
            if right < left:
                return [None]
            if right == left:
                return [TreeNode(left)]
            tmp_ans = []
            for root in range(left, right+1):
                left_sub_trees = dfs(left, root-1)   ## bug:忘记了范围是从1开始
                right_sub_trees = dfs(root+1, right)
                for l in left_sub_trees:
                    for r in right_sub_trees:
                        tree_root = TreeNode(val=root, left=l, right=r)
                        tmp_ans.append(tree_root)
            return tmp_ans

        ret = dfs(1, n)
        print("ans", len(ret))
        return ret

    # 自顶向下的动态规划，自定义mem进行存储
    def generateTrees_dp(self, n: int) -> List[Optional[TreeNode]]:
        def dfs(left, right, mem):
            if right < left:
                return [None]
            if (left, right) in mem:
                return mem[(left, right)]
            tmp_ans = []
            for root in range(left, right+1):
                left_sub_trees = dfs(left, root-1, mem)
                right_sub_trees = dfs(root+1, right, mem)
                for l in left_sub_trees:
                    for r in right_sub_trees:
                        tree_root = TreeNode(val=root, left=l, right=r)
                        tmp_ans.append(tree_root)
            mem[(left, right)] = tmp_ans
            return tmp_ans

        ret = dfs(1, n, {})
        # print(ret)
        return ret

    # 自底向上dp
    def generateTrees_dp(self, n: int) -> List[Optional[TreeNode]]:
        mem = []
        for i in range(1, n+1):
            for j in range(1, n+1):
                pass
        return ret

su = Solution()
n = 3
su.generateTrees(n)
        