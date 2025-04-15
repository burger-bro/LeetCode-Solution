# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        dummy_head = ListNode(-float("inf"))
        cur = head
        
        while cur is not None:
            
            # print_list(dummy_head)

            dummy_cur = dummy_head
            pre = None
            while dummy_cur is not None:
                if dummy_cur.val > cur.val:
                    break
                pre = dummy_cur
                dummy_cur = dummy_cur.next

            tmp = cur
            cur = cur.next
            tmp.next = None

            pre.next = tmp
            if dummy_cur:
                tmp.next = dummy_cur

        return dummy_head.next
        

def build_list(array):
    dummy = ListNode()
    cur = dummy
    for n in array:
        cur.next = ListNode(n)
        cur = cur.next
    return dummy.next

def print_list(head):
    print("***** start *****")
    while head:
        print(head.val, end='')
        head = head.next
    print('')
    print("***** ----- *****")

su = Solution()

# case 
head = [3, 4, 1]
head = build_list(head)
res = su.insertionSortList(head)
print_list(res)

# case 
head = [3]
head = build_list(head)
res = su.insertionSortList(head)
print_list(res)

# case 
head = [2, 1]
head = build_list(head)
res = su.insertionSortList(head)
print_list(res)

# case std1
head = [4,2,1,3]
head = build_list(head)
res = su.insertionSortList(head)
print_list(res)

# case std2
head = [-1,5,3,4,0]
head = build_list(head)
res = su.insertionSortList(head)
print_list(res)

