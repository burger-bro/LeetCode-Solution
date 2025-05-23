from typing import List, Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        cur = head
        last = dummy
        while cur is not None:
            nex = cur.next
            # print("loop", cur.val)
            if nex is not None and nex.val == cur.val:
                last_dup = nex
                while nex is not None and nex.val == cur.val:
                    # print("n", nex.val)
                    # print("n_id", id(nex))
                    last_dup = nex
                    nex = nex.next
                last.next = last_dup.next
                # print("concat", id(last), id(last_dup.next))
                cur = last.next
                continue
            last = cur
            cur = cur.next

        return dummy.next


def build_list(l: List) -> ListNode:
    if not l: return None
    root = ListNode(l[0])
    p = root
    for e in l[1:]:
        p.next = ListNode(e)
        p = p.next
    return root

def print_list(l: ListNode) -> ListNode:
    p = l
    while p is not None:
        print(p.val, id(p))
        p = p.next

def check_list(a, b):
    p, q = a, b
    while p is not None or q is not None:
        if p.val != q.val:
            raise AssertionError
        p, q = p.next, q.next
    if not (p is None and q is None):
        raise AssertionError

su = Solution()

# case std 1
head = [1,2,3,3,4,4,5]
ans = [1, 2, 5]
head = build_list(head)
ans = build_list(ans)
head = su.deleteDuplicates(head)
check_list(head, ans)

# case std 2
head = [1,1,1,2,3]
ans = [2, 3]
head = build_list(head)
ans = build_list(ans)
head = su.deleteDuplicates(head)
check_list(head, ans)

# case boundry list len 0
head = []
ans = []
head = build_list(head)
ans = build_list(ans)
head = su.deleteDuplicates(head)
check_list(head, ans)

# case boundry list len 1
head = [1]
ans = [1]
head = build_list(head)
ans = build_list(ans)
head = su.deleteDuplicates(head)
check_list(head, ans)

# case boundry list len 2
head = [1, 2]
ans = [1, 2]
head = build_list(head)
ans = build_list(ans)
head = su.deleteDuplicates(head)
check_list(head, ans)

# case boundry list len 2 void
head = [2, 2]
ans = []
head = build_list(head)
ans = build_list(ans)
head = su.deleteDuplicates(head)
check_list(head, ans)

# case boundry list len 300
head = [1 for _ in range(300)] + [2]
ans = [2]
head = build_list(head)
ans = build_list(ans)
head = su.deleteDuplicates(head)
check_list(head, ans)

# case categery 234444456
head = [2,3,4,4,4,4,4,5,6]
ans = [2,3,5,6]
head = build_list(head)
ans = build_list(ans)
head = su.deleteDuplicates(head)
check_list(head, ans)

# case categery 444445679
head = [4,4,4,4,4,5,6,7,9]
ans = [5,6,7,9]
head = build_list(head)
ans = build_list(ans)
head = su.deleteDuplicates(head)
check_list(head, ans)

# case categery 012344444
head = [0,1,2,3,4,4,4,4,4]
ans = [0,1,2,3]
head = build_list(head)
ans = build_list(ans)
head = su.deleteDuplicates(head)
check_list(head, ans)

# case categery 111222333444555
head = [1,1,1,2,2,2,3,3,3,4,4,4,5,5,5]
ans = []
head = build_list(head)
ans = build_list(ans)
head = su.deleteDuplicates(head)
check_list(head, ans)

# case categery 11223344556788899
head = [1,1,2,2,3,3,4,4,5,5,6,7,8,8,8,9,9]
ans = [6,7]
head = build_list(head)
ans = build_list(ans)
head = su.deleteDuplicates(head)
check_list(head, ans)