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

# def build_tree2(array):
#     root = None

class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        case1: adjacent left 
        case2: adjacent right 
        both case1 and case2 can keep track of the first wrong node, and when the traverse is end,
        if there is only one error node, then exchange them.(??what about the adjacent wrong again?)
        case3: farther node 
        """
        suspicious_nodes = []
        def recurse(node):
            if node is None:
                return
            if node.left is not None and node.left >= node.val:
                suspicious_nodes.append(node)
            if node.right is not None and node.right <= node.val:
                suspicious_nodes.append(node)
        if len(suspicious_nodes) == 1:
            node = suspicious_nodes[0]
            if node.left is not None and node.val >= node.left.val:
                node.left.val, node.val = node.val, node.left.val
            elif node.right is not None and node.val <= node.right.val:
                node.right.val, node.val = node.val, node.right.val
        elif len(suspicious_nodes) == 2:
            node = suspicious_nodes[0]
            if (node.left is not None and node.left is suspicious_nodes[1]) or (node.right is not None and node.right is suspicious_nodes[0]):
                pass
            else:
                suspicious_nodes[0].val, suspicious_nodes[1].val = suspicious_nodes[1].val, suspicious_nodes[0].val

    def recoverTree(self, root: Optional[TreeNode]) -> None:
        def validate_bst(node):
            if node is None:
                return True
            if node.left is not None and node.left.val >= node.val:
                return False
            if node.right is not None and node.right.val <= node.val:
                return False
            return validate_bst(node.left) and validate_bst(node.right)

        def traverse(node):
            if node is None:
                return
            node_list.append(node)
            traverse(node.left)
            traverse(node.right)
        # print(validate_bst(root))
        node_list = []
        traverse(root)
        for i in node_list:
            for j in node_list[1:]:
                i.val, j.val = j.val, i.val
                if validate_bst(root):
                    return root
                i.val, j.val = j.val, i.val

    def recoverTree(self, root: Optional[TreeNode]) -> None:
        def traverse(node):
            if node is None:
                return
            traverse(node.left)
            node_list.append(node)
            traverse(node.right)
        node_list = []
        traverse(root)
        tmp, tmp_idx = None, None
        for i in range(1, len(node_list)):
            if node_list[i].val < node_list[i-1].val:
                if tmp is not None:
                    tmp, node_list[i-1] = node_list[i-1], tmp
                    return root
                tmp = node_list[i-1]
                tmp_idx = i-1
        tmp, node_list[tmp_idx+1] = node_list[tmp_idx+1], tmp
        return root
        
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        def traverse(node):
            if node is None:
                return
            traverse(node.left)
            nodes.append(node)
            traverse(node.right)
        nodes = []
        traverse(root)

        for i in nodes:
            print(i.val, end='')
        print('')

        values = []
        for n in nodes:
            values.append(n.val)
        values_sorted = sorted(values)
        
        exchange = []
        for i in range(len(values_sorted)):
            if values_sorted[i] != values[i]:
                exchange.append(i)
        nodes[exchange[0]], nodes[exchange[1]] = nodes[exchange[1]], nodes[exchange[0]]

        return root

    def recoverTree(self, root: Optional[TreeNode]) -> None:
        def traverse(node):
            if node is None:
                return
            traverse(node.left)
            nodes.append(node)
            traverse(node.right)
        nodes = []
        traverse(root)

        prev, start, end = None, None, None
        for n in nodes:
            if prev is not None and prev.val > n.val:
                if start is None:
                    start = prev
                end = root
            prev = root
        start.val, end.val = end.val, start.val
        return root

su = Solution()
root = [1,3,2]
root = TreeNode(1,left=TreeNode(3,right=TreeNode(2)))
print_tree(root)
res = su.recoverTree(root)
print_tree(root)

        