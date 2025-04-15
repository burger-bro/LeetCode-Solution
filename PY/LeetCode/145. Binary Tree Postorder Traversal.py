from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def print_stack(stack):
    print('stack')
    for n in stack:
        print(n.val, end=' ')
        
    print(' ')

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        ans = []
        node = root
        flg = "left"
        cnt = 0
        while node or stack:
            cnt += 1
            if cnt < 10:
                print("*************")
                print(flg)
                print_stack(stack)
                print(ans)

            if flg == "left":
                node = node if node else stack.pop()
                while node is not None:
                    stack.append(node)
                    node = node.left
                flg = "right"
                continue

            if flg == "right":
                node = node if node else stack[-1]
                if node.right:
                    flg = "left"
                    stack.append(node.right)
                    node = None
                else:
                    flg = "mid" 
                continue
            
            if flg == "mid":
                if cnt < 15:
                    print("-----------")
                    print("?")
                    print_stack(stack)
                    print(ans)
                    print("res:", node, stack)
                    # exit(0)
                    print("-----------")
                
                node = stack.pop()
                ans.append(node.val)
                flg = "right"

                node = None

                continue
            # print("ans:", ans)
        return ans

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        node = root
        while node or stack:
            while node is not None:
                stack.append((node, 'l'))
                node = node.left
            node, flg = stack.pop()
            if flg == 'l':
                if node.right:
                    flg = "r"
                    stack.append((node.right, 'r'))
                    node = None
                else:
                    flg = "mid" 
                continue
su = Solution()

head = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
head.right = node2
node2.left = node3
su.postorderTraversal(head)


