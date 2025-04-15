class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(array):
    """
    input: an array represents a b_t: None is inplacement
    output: root node for the b_t
    """
    def dfs(i):
        if i >= len(array): return None
        node = TreeNode(array[i])
        node.left = dfs(2*i)
        node.right = dfs(2*i+1)
        return node
    return dfs(1)

def print_tree(node: TreeNode):
    if node is None: return
    print(node.val)
    print_tree(node.left)
    print_tree(node.right)

def preorder(node: TreeNode):
    ans = []
    def dfs(node: TreeNode):
        if node is None: return
        ans.append(node.val)
        dfs(node.left)
        dfs(node.right)
    dfs(node)
    return ans

def inorder(node: TreeNode):
    ans = []
    def dfs(node: TreeNode):
        if node is None: return
        dfs(node.left)
        ans.append(node.val)
        dfs(node.right)
    dfs(node)
    return ans

def postorder(node: TreeNode):
    ans = []
    def dfs(node: TreeNode):
        if node is None: return
        dfs(node.left)
        dfs(node.right)
        ans.append(node.val)
    dfs(node)
    return ans

def preorder_tra(node: TreeNode):
    ans = []
    stack = []
    n = node
    while n is not None:
        ans.append(n.val)
        stack.append(n)
        n = n.left

    while stack:
        n = stack.pop()
        t = n.right
        while t is not None:
            ans.append(t.val)
            stack.append(t)
            t = t.left

    return ans

def inorder_tra(node: TreeNode):
    ans = []
    stack = []
    n = node
    while n is not None:
        stack.append(n)
        n = n.left

    while stack:
        n = stack.pop()
        ans.append(n.val)
        t = n.right
        while t is not None:
            stack.append(t)
            t = t.left
    return ans

def postorder_tra(node: TreeNode):
    ans = []
    stack = []
    n = node
    while n is not None:
        ans.append(n.val)
        stack.append(n)
        n = n.right

    while stack:
        n = stack.pop()
        t = n.left
        while t is not None:
            ans.append(t.val)
            stack.append(t)
            t = t.right
    return ans[::-1]

def preorder_tra2(node: TreeNode):
    stack = [] 
    ans = []
    if node is not None: 
        stack.append(node)
    while stack:
        if stack[-1] is not None:
            n = stack.pop()
            n.right and stack.append(n.right)
            n.left and stack.append(n.left)
            stack.append(n)
            stack.append(None)
        else:
            stack.pop()
            t = stack.pop()
            ans.append(t.val)
    return ans
            
def inorder_tra2(node: TreeNode):
    stack = [] 
    ans = []
    if node is not None: 
        stack.append(node)
    while stack:
        if stack[-1] is not None:
            n = stack.pop()
            n.right and stack.append(n.right)
            stack.append(n)
            stack.append(None)
            n.left and stack.append(n.left)
        else:
            stack.pop()
            t = stack.pop()
            ans.append(t.val)
    return ans

def postorder_tra2(node: TreeNode):
    stack = [] 
    ans = []
    if node is not None: 
        stack.append(node)
    while stack:
        if stack[-1] is not None:
            n = stack.pop()
            stack.append(n)
            stack.append(None)
            n.right and stack.append(n.right)
            n.left and stack.append(n.left)
        else:
            stack.pop()
            t = stack.pop()
            ans.append(t.val)
    return ans


tt = [None,1,2,3,4,5,365,235,262,999,533]
tt = build_tree(tt)
print(preorder(tt))
print(preorder_tra(tt))
print(preorder_tra2(tt))
assert(preorder(tt) == preorder_tra(tt))
assert(inorder(tt) == inorder_tra(tt))
assert(postorder(tt) == postorder_tra(tt))
assert(preorder(tt) == preorder_tra2(tt))
assert(inorder(tt) == inorder_tra2(tt))
assert(postorder(tt) == postorder_tra2(tt))

# start = 20
# sum = 0
# for i in range(20):
#     sum += start
#     start *= 1.1
#     print(sum)
# print(sum)
