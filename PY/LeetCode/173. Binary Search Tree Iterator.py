# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root):
        self.pointer = 0
        self.array = []
        def dfs(p):
            if p is None: return
            dfs(p.left)
            self.array.append(p.val)
            dfs(p.right)
        dfs(root)

    def next(self) -> int:
        ret = self.array[self.pointer]
        self.pointer += 1
        return ret
    

    def hasNext(self) -> bool:
        return self.pointer >= len(self.array)

class BSTIterator:
    def __init__(self, root):
        self.stack = []
        self.push_all(root)

    def push_all(self, node):
        while node is not None:
            self.stack.append(node)
            node = node.left
        
    def next(self) -> int:
        ret = self.stack.pop()
        if ret.right is not None:
            self.push_all(ret.right)
        return ret.val
    

    def hasNext(self) -> bool:
        return True if self.stack else False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()