# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def get_mid(self, node):
        fast, slow = node, node
        while fast.next:
            if fast.next.next:
                fast = fast.next.next
            else:
                break
            slow = slow.next
        
        ret = slow.next
        slow.next = None
        return ret

    def merge(self, q1, q2):
        node1, node2 = q1, q2
        dummy = ListNode(-float("inf"))
        cur = dummy
        pre = None
        while node1 and node2:
            if node1.val < node2.val:
                pre = node1
                node1 = node1.next
            else:
                pre = node2
                node2 = node2.next
            cur.next = pre
            cur = cur.next

        if node1:
            cur.next = node1
        if node2:
            cur.next = node2

        return dummy.next

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None    
        if head.next is None:
            return head
        left = head
        right = self.get_mid(head)

        left = self.sortList(left)
        right = self.sortList(right)

        return self.merge(left, right)
            
def build_list(array):
    dummy = ListNode()
    cur = dummy
    for n in array:
        cur.next = ListNode(n)
        cur = cur.next
    return dummy.next

def print_list(head):
    print("***** start *****")
    p = head
    while p:
        print(p.val, end='')
        p = p.next
    print('')
    print("***** ----- *****")

su = Solution()


# case std1
head = [4,2,1,3]
head = build_list(head)
res = su.sortList(head)
print_list(res)


# case std2
head = [-1,5,3,4,0]
head = build_list(head)
res = su.sortList(head)
print_list(res)


# case 
head = [3, 4, 1]
head = build_list(head)
res = su.sortList(head)
print_list(res)
# exit(0)

# case 
head = [3]
head = build_list(head)
res = su.sortList(head)
print_list(res)

# case 
head = [2, 1]
head = build_list(head)
res = su.sortList(head)
print_list(res)


