from typing import Optional
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        """
        先遍历到所有叶子节点，再返回？root -> node1 2 3 4 5 -> node 7 8 9 10 11

        逐个处理，对于每一个遇到的节点，先new一个node，难点在于如何搜集他的所有neighbors
        可以用一个dict来存储node->node_neighbors的映射，每个节点存储时，只记录neighbor的val。
        是否需要visited？
        """
        if node is None: return None
        val_node_map = {}
        def traverse(node: Node):
            if node.val in val_node_map:
                return
            new_node = Node(node.val, [n.val for n in node.neighbors])
            if new_node not in val_node_map:
                val_node_map[node.val] = new_node
            for n in node.neighbors:
                traverse(n)

        traverse(node)
        for val, node in val_node_map.items():
            for i in range(len(node.neighbors)):
                node.neighbors[i] = val_node_map[node.neighbors[i]]
        
        for val, node in val_node_map.items():
            print(val, ":")
            for n in node.neighbors:
                print("n", n.val)
        return val_node_map[1]

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None: return None
        old_new_pairs: Optional['Node'] = {}
        def dfs(node: Node):
            if node in old_new_pairs:
                return old_new_pairs[node]
            old_new_pairs[node] = Node(node.val)
            for n in node.neighbors:
                old_new_pairs[node].neighbors.append(dfs(n))
            return old_new_pairs[node]
        return dfs(node)

su = Solution()
# case1
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n1.neighbors=[n2, n4]
n2.neighbors=[n1, n3]
n3.neighbors=[n2, n4]
n4.neighbors=[n1, n3]
su.cloneGraph(n1)
# case2
# su.cloneGraph()

