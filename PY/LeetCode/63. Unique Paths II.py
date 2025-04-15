from typing import List
from collections import deque
from functools import cache

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n, m = len(obstacleGrid), len(obstacleGrid[0])
        queue = deque([(0, 0)])
        directions = ((0, 1), (1, 0))
        ret = 0
        while queue:
            x, y = queue.popleft()
            if x == n-1 and y == m-1 and obstacleGrid[x][y] == 0:
                ret += 1
                continue
            for d in directions:
                new_x, new_y = x + d[0], y + d[1]
                if 0 <= new_x < n and 0 <= new_y < m and obstacleGrid[new_x][new_y] == 0:
                    queue.append((new_x, new_y))
        print(ret)
        return ret            

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n, m = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1 or obstacleGrid[n-1][m-1] == 1: return 0
        directions = ((0, -1), (-1, 0))
        @cache
        def recursive(pos: tuple):
            x, y = pos
            if x == 0 and y == 0:
                return 1
            ways = 0
            for d in directions:
                n_x, n_y = x + d[0], y + d[1]
                if 0 <= n_x < n and 0 <= n_y < m and obstacleGrid[n_x][n_y] == 0:
                    ways += recursive((n_x, n_y))
            return ways
        ret = recursive((n-1, m-1))
        print(ret)
        return ret   
    
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n, m = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1 or obstacleGrid[n-1][m-1] == 1: return 0
        dp = [[0] * m for _ in range(n)]
        dp[0][0] = 1
        for i in range(1, m):
            if obstacleGrid[0][i] == 1:
                break
            dp[0][i] += dp[0][i-1]
        for i in range(1, n):
            if obstacleGrid[i][0] == 1:
                break
            dp[i][0] += dp[i-1][0]
        for i in range(1, n):
            for j in range(1, m):
                if obstacleGrid[i][j] == 1:
                    continue
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]


su = Solution()
# case1
obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
res = su.uniquePathsWithObstacles(obstacleGrid)
ans = 2
assert(res == ans)

# case2
obstacleGrid = [[0,1],[0,0]]
res = su.uniquePathsWithObstacles(obstacleGrid)
ans = 1
assert(res == ans)

# case3 - 最小值
obstacleGrid = [[0]]
res = su.uniquePathsWithObstacles(obstacleGrid)
ans = 1
assert(res == ans)

# case4 - 横
obstacleGrid = [[0, 0, 0, 0, 0, 0, 0, 0]]
res = su.uniquePathsWithObstacles(obstacleGrid)
ans = 1
assert(res == ans)

# case5 - 横，死路
obstacleGrid = [[0, 0, 0, 0, 1, 0, 0, 0]]
res = su.uniquePathsWithObstacles(obstacleGrid)
ans = 0
assert(res == ans)

# case6 - 竖，死路
obstacleGrid = [[0], [0], [0], [0], [1], [0], [0], [0]]
res = su.uniquePathsWithObstacles(obstacleGrid)
ans = 0
assert(res == ans)

# case6 - 对角线，死路
obstacleGrid = [[1, 0, 0, 0], 
                [0, 1, 0, 0], 
                [0, 0, 1, 0], 
                [0, 0, 0, 0]]
res = su.uniquePathsWithObstacles(obstacleGrid)
ans = 0
assert(res == ans)

# case7 - 最小值, 无解
obstacleGrid = [[1]]
res = su.uniquePathsWithObstacles(obstacleGrid)
ans = 0
assert(res == ans)

# case8 - 出发点死路
obstacleGrid = [[1], [0]]
res = su.uniquePathsWithObstacles(obstacleGrid)
ans = 0
assert(res == ans)

# case9 - perf
obstacleGrid = [[0,0,0,0,0,1,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,1,0,0,0,0,1,0,1,0,1,0,0],[1,0,0,0,0,0,1,0,0,0,0,0,1,0,1,1,0,1],[0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0],[0,0,0,0,0,1,0,0,0,0,1,1,0,1,0,0,0,0],[1,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,1,0],[0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0],[0,0,1,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0],[0,1,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0],[0,0,1,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1],[0,1,0,1,0,1,0,0,0,0,0,0,0,1,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1],[1,0,1,1,0,0,0,0,0,0,1,0,1,0,0,0,1,0],[0,0,0,1,0,0,0,0,1,1,1,0,0,1,0,1,1,0],[0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,1,1,0,0,1,0,0,0,0,0,0,0,1,1,0,0,0],[0,0,0,0,0,0,1,0,1,0,0,1,0,1,1,1,0,0],[0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,1,1],[0,1,0,0,0,0,0,0,0,0,1,0,1,0,1,0,1,0],[1,0,0,1,0,1,0,0,1,0,0,0,0,0,0,0,0,0],[0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0],[0,1,0,0,0,0,0,1,0,0,0,0,0,0,1,1,1,0],[1,0,1,0,1,0,0,0,0,0,0,1,1,0,0,0,0,1],[1,0,0,0,0,0,1,1,0,0,0,1,0,0,0,0,0,0]]
res = su.uniquePathsWithObstacles(obstacleGrid)
ans = 13594824
assert(res == ans)