from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
"""
0 1 2 3 4 5 6 7 8 9

0  1   2   3   4   5
n n-1 n-2 n-3 n-4 n-5

0 1 2 3 4
 9 8 7 6 5

0 1 2 3 4
 8 7 6 5

1 2 3 4
 7 6 5

1 2 3
 5 4

1 2
 4 3
 
"""
class Solution:
    # def reorderList(self, head: Optional[ListNode]) -> None:
    #     p1 = p2 = head
    #     def recursive(p1, p2):
    #         p1 = p1.next
    #         if p2.next and p2.next.next:
    #             p2 = p2.next.next
    #         else:
    #             return p2
    #         ret_p2 = recursive(p1, p2)
    #         print(p1.val, p2.val, ret_p2.val)
    #         p1.next = ret_p2
    #         ret_p2 = ret_p2.next
    #         ret_p2.next = p1
    #         return ret_p2
    #     return recursive(p1, p2)

    def reorderList(self, head: Optional[ListNode]) -> None:
        p1 = p2 = head
        stack = []
        flag = False
        once = True
        while p2:
            stack.append(p1)
            p1 = p1.next
            if p2.next:
                p2 = p2.next.next
            else:
                flag = True
                print("yes?")
                break
        print(stack)
        prv = p1
        if flag:
            tmp = stack.pop()
            print("tmp.val:", tmp.val)
        # if flag:
        #     t = stack.pop()
        #     t.next = None
        #     p1.next = t
        while stack:
            t = stack.pop()
            print("t.val:", t.val, t.next)
            print("p1.val:", p1.val, p1.next)
            t.next = p1
            if t is head:
                break
            tp = p1
            p1 = p1.next
            p1.next = t

            if once and prv:
                if flag:
                    prv.next = tmp
                    tmp.next = None
                else:
                    prv.next = None
                once = False

        if once and prv:
            if flag:
                prv.next = tmp
                tmp.next = None
            else:
                prv.next = None
            once = False

        return head

    def reorderList(self, head: Optional[ListNode]) -> None:
        p1 = p2 = head
        stack = []
        stack2 = []
        flag = False
        while p2:
            stack.append(p1)
            p1 = p1.next
            if p2.next:
                p2 = p2.next.next
            else:
                flag = True
                print("yes?")
                break
        while p1:
            stack2.append(p1)
            p1 = p1.next
        stack2 = stack2[::-1]
        def merge(s1, s2):
            if len(s1) > len(s2):
                head.next = merge(s2, s1)
                return
            last = None
            while s1 and s2:
                t1 = s1.pop()
                t2 = s2.pop()
                print("t1 t2", t1.val, t2.val)
                t1.next = t2
                t2.next = last
                last = t1
            return last
        print(stack)
        print(stack2)
        merge(stack, stack2)
        return head

su = Solution()
def print_list(node):
    cnt = 10
    while node is not None:
        cnt -= 1
        if not cnt:
            break
        print(node.val)
        node = node.next

a1 = ListNode(1)
a2 = ListNode(2)
a3 = ListNode(3)
a4 = ListNode(4)
a5 = ListNode(5)
a6 = ListNode(6)
a7 = ListNode(7)
a1.next = a2
a2.next = a3
a3.next = a4
a4.next = a5
a5.next = a6
a6.next = a7
res = su.reorderList(a1)
print_list(res)
