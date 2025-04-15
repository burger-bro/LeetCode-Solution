# Definition for a binary tree node.
from collections import deque

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def printTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[str]]
        """
        height = -1
        queue = deque([root])
        while queue:
            height += 1
            cur_level = []
            while queue:
                cur_level.append(queue.popleft())
            for n in cur_level:
                n.left is not None and queue.append(n.left)
                n.right is not None and queue.append(n.right)
        print(height)

        def get_hegiht(node):
            if node is None:
                return 0
            return 1+max(get_hegiht(node.left), get_hegiht(node.right))
        height = get_hegiht(root)-1

        m, n = height+1, 2**(height+1)-1
        res = [[""] * (n) for _ in range(m)]
        print(res)


        r = 0
        c = (n-1)//2 # +1 ?
        res[0][c] = str(root.val)
        queue = deque([[root, c]])
        while queue:
            cur_level = []
            while queue:
                cur_level.append(queue.popleft())
            print("cur", cur_level)
            for n, c in cur_level:
                if n.left is not None:
                    new_c = c-2**(height-r-1)
                    res[r+1][new_c] = str(n.left.val)
                    queue.append([n.left, new_c])
                if n.right is not None:
                    new_c = c+2**(height-r-1)
                    res[r+1][new_c] = str(n.right.val)
                    queue.append([n.right, new_c])
            r += 1
        
        print(res)
        return res
            
su = Solution()

dummy = TreeNode(val=1, left=TreeNode(2,right=TreeNode(4)), right=TreeNode(3))

su.printTree(dummy)


