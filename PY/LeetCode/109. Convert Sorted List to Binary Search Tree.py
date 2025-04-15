from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        nums = []
        while head is not None:
            nums.append(head.val)
            head = head.next
        def dfs(left, right):
            if left == right:
                tmp = nums[right]
                return TreeNode(tmp)
            mid = (left + right) // 2
            l_tree = dfs(left, mid-1) if left != mid else None
            r_tree = dfs(mid+1, right)
            return TreeNode(nums[mid], l_tree, r_tree)
        return dfs(0, len(nums)-1) if nums else None
    
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        def get_mid(head: ListNode) -> ListNode:
            fast = head
            slow = head
            prev = None
            while fast and fast.next:
                fast = fast.next.next
                prev = slow
                slow = slow.next
            if prev:
                prev.next = None
            return slow
        def dfs(_head):
            if _head is None:
                return None
            if _head.next is None:
                return TreeNode(_head.val)
            mid = get_mid(_head)
            print(mid.val)
            r_tree = dfs(mid.next)
            mid.next = None
            l_tree = dfs(_head)
            return TreeNode(mid.val, l_tree, r_tree)
        return dfs(head)

def build(l):
    head = ListNode(0)
    p = head
    for v in l:
        p.next = ListNode(v)
        p = p.next
    return head.next

def get_mid(head):
    fast, slow, prev = head, head, head
    while fast is not None and fast.next is not None:
        prev = slow
        fast = fast.next.next
        slow = slow.next
    return prev if fast is None else slow

def get_mid(head: ListNode) -> ListNode:
    fast = head
    slow = head
    prev = None
    while fast and fast.next:
        fast = fast.next.next
        prev = slow
        slow = slow.next
    if prev:
        prev.next = None
    return slow

su = Solution()
link_list = build([1])
print(getMiddle(link_list).val)
# su.sortedListToBST(link_list)