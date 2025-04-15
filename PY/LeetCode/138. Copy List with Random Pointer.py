from typing import Optional
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        old_new_pairs = {}
        def dfs(node):
            if node is None:
                return
            if node in old_new_pairs: return old_new_pairs[node] 
            new_node = Node(node.val, dfs(node.next), dfs(node.random))
            old_new_pairs[node] = new_node
            return new_node

        return dfs(head)

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        old_new_pairs = {}
        def dfs(node):
            if node is None:
                return
            if node in old_new_pairs: return old_new_pairs[node] 
            new_node = Node(node.val)
            old_new_pairs[node] = new_node
            new_node.next = dfs(node.next)
            new_node.random = dfs(node.random)
            return new_node

        return dfs(head)


