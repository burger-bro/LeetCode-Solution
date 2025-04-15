from typing import Optional, List
from collections import deque
import heapq

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from dataclasses import dataclass, field
from typing import Any

@dataclass(order=True)
class PrioritizedItem:
    priority: int
    item: Any=field(compare=False)

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque([(root, 0)])
        ret = []
        while queue:
            node, level = queue.popleft()
            if node is None:
                continue
            if level > len(ret) - 1:
                ret.append([])
            ret[level].append(node.val)
            queue.append((node.left, level+1))
            queue.append((node.right, level+1))
        return ret

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        heap = [PrioritizedItem(0, root)]
        heapq.heapify(heap)
        ret = []
        while heap:
            level, node = heapq.heappop(heap)
            if node is None:
                continue
            if level > len(ret) - 1:
                ret.append([])
            ret[level].append(node.val)
            heapq.heappush(PrioritizedItem(level+1, node.left))
            heapq.heappush(PrioritizedItem(level+1, node.right))
        return ret  
        



su = []
