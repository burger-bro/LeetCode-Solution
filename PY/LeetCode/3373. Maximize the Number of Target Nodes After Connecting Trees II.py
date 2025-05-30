from typing import List
from collections import defaultdict

class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        def dfs(cur, cnt, _tree, _visited, k):
            target_num = 1 if cnt%2 == k else 0
            for nxt in _tree[cur]:
                if not _visited[nxt]:
                    _visited[nxt] = True
                    target_num += dfs(nxt, cnt+1, _tree, _visited, k)
            # print(cur, cnt, target_num)
            return target_num
            
        def get_target(edges, k):
            tree = defaultdict(list)
            for edge in edges:
                tree[edge[0]].append(edge[1])
                tree[edge[1]].append(edge[0])
            print(tree)
            target_num = [-1]*len(tree)
            for i in range(len(tree)):
                visited = [False]*len(tree)
                visited[i] = True
                target_num[i] = dfs(i, 0, tree, visited, k)
            # print("target_num", target_num)
            return target_num

        ret = get_target(edges1, 0)
        tree2_max = max(get_target(edges2, 1))
        return [n+tree2_max for n in ret]

        # for i in range(len(tree)):




su = Solution()

# case std1 
edges1 = [[0,1],[0,2],[2,3],[2,4]]
edges2 = [[0,1],[0,2],[0,3],[2,7],[1,4],[4,5],[4,6]]
res = su.maxTargetNodes(edges1, edges2)
print("res", res)
ans = [8,7,7,8,8]
assert(res == ans)
