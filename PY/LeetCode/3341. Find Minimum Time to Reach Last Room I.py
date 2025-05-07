from typing import List
from functools import lru_cache, cache
import heapq

class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n = len(moveTime)
        m = len(moveTime[0])
        @lru_cache
        def dfs(i, j):
            if i==0 and j==0:
                return 0
            up = max(dfs(i-1, j), moveTime[i][j]) if 0 <= i-1 < n else float("inf")
            left = max(dfs(i, j-1), moveTime[i][j]) if 0 <= j-1 < m else float("inf")
            tmp_ret = min(up, left) + 1
            print(i, j, tmp_ret, up, left)
            return tmp_ret

        ret = dfs(n-1, m-1)
        print(ret)
        return ret

    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        if not moveTime or not moveTime[0]:
            return 0
        
        n, m = len(moveTime), len(moveTime[0])
        heap = []
        heapq.heappush(heap, (0, 0, 0))  # (current_time, i, j)
        visited = [[float('inf')] * m for _ in range(n)]
        visited[0][0] = 0  # 初始时间
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 上、下、左、右
        
        while heap:
            current_time, i, j = heapq.heappop(heap)
            if i == n - 1 and j == m - 1:
                return current_time  # 到达终点
            
            if current_time > visited[i][j]:
                continue  # 已经存在更优解
            
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < n and 0 <= nj < m:
                    # 计算到达 (ni, nj) 的时间
                    new_time = max(current_time + 1, moveTime[ni][nj])
                    if new_time < visited[ni][nj]:
                        visited[ni][nj] = new_time
                        heapq.heappush(heap, (new_time, ni, nj))
        
        return -1  # 如果无法到达终点（根据题意，可能不需要）


su = Solution()
# case bug
moveTime = [[94,79,62,27,69,84],[6,32,11,82,42,30]]
res = su.minTimeToReach(moveTime)
ans = 72
assert(res == ans)

# case bug
moveTime = [[56,93],[3,38]]
res = su.minTimeToReach(moveTime)
ans = 39
assert(res == ans)

# case std1
moveTime = [[0,4],[4,4]]
res = su.minTimeToReach(moveTime)
ans = 6
assert(res == ans)

# case std1
moveTime = [[0,0,0],[0,0,0]]
res = su.minTimeToReach(moveTime)
ans = 3
assert(res == ans)
