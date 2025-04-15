from typing import List
from collections import deque, namedtuple


class Solution:
    def minPathSum0(self, grid: List[List[int]]) -> int:
        position = namedtuple("position", "index sum")
        queue = deque([position((0, 0), grid[0][0])])
        end = (len(grid) - 1, len(grid[0]) - 1) 
        min_sum = float("inf")
        while queue:
            cur_index, cur_sum = queue.popleft()
            # print(cur_index, cur_sum)
            if cur_index == end:
                min_sum = min(min_sum, cur_sum)
                continue
            # if cur_sum > min_sum:
            #     continue
            m, n = cur_index
            if m < len(grid) - 1 and cur_sum + grid[m + 1][n] <= min_sum:
                queue.append(position((m + 1, n), cur_sum + grid[m + 1][n]))
            if n < len(grid[0]) - 1 and cur_sum + grid[m][n + 1] <= min_sum:
                queue.append(position((m, n + 1), cur_sum + grid[m][n + 1]))
        print(min_sum)
        return min_sum

    def minPathSum0(self, grid: List[List[int]]) -> int:
        position = namedtuple("position", "index sum")
        end = (len(grid) - 1, len(grid[0]) - 1) 
        min_sum = float("inf")
        def recursive(pos):
            nonlocal min_sum
            cur_index, cur_sum = pos
            if cur_index == end:
                min_sum = min(min_sum, cur_sum)
                return 
            if cur_sum > min_sum:
                return
            m, n = cur_index
            if m < len(grid) - 1 and cur_sum + grid[m + 1][n] <= min_sum:
                recursive(position((m + 1, n), cur_sum + grid[m + 1][n]))
            if n < len(grid[0]) - 1 and cur_sum + grid[m][n + 1] <= min_sum:
                recursive(position((m, n + 1), cur_sum + grid[m][n + 1]))

        recursive(position((0, 0), grid[0][0]))
        # print(min_sum)
        return min_sum

    def minPathSum0(self, grid: List[List[int]]) -> int:
        end = (len(grid) - 1, len(grid[0]) - 1) 
        memo = [[-1] * (end[1] + 1) for _ in range(end[0] + 1)]
        def recursive(idx):
            if idx == (0, 0):
                return grid[0][0]
            m, n = idx
            if memo[m][n] != -1:
                return memo[m][n]
            up = recursive((m-1, n)) if m - 1 >= 0 else float("inf")
            left = recursive((m, n-1)) if n - 1 >= 0 else float("inf")
            # print(m, n, up, left)
            ans = min(grid[m][n] + up, grid[m][n] + left)
            memo[m][n] = ans
            return ans

        min_sum = recursive(end)
        # print(min_sum)

        return min_sum

    def minPathSum(self, grid: List[List[int]]) -> int:
        end = (len(grid), len(grid[0])) 
        for i in range(1, end[0]):
            grid[i][0] += grid[i-1][0]
        for i in range(1, end[1]):
            grid[0][i] += grid[0][i-1]
        for i in range(1, end[0]):
            for j in range(1, end[1]):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        # print(min_sum)
        print(grid)
        return grid[-1][-1]

su = Solution()
grid = [[1,3,1],[1,5,1],[4,2,1]]
ans1 = 7
res = su.minPathSum(grid)
assert(ans1 == res)
grid = [[1,2,3],[4,5,6]]
ans2 = 12
res = su.minPathSum(grid)
assert(ans2 == res)

grid = [[1,2,3]]
ans3 = 6
res = su.minPathSum(grid)
assert(ans3 == res)

grid = [[1,1,1], [0,0,0]]
ans4 = 1
res = su.minPathSum(grid)
assert(ans4 == res)

grid = [[7,1,3,5,8,9,9,2,1,9,0,8,3,1,6,6,9,5],[9,5,9,4,0,4,8,8,9,5,7,3,6,6,6,9,1,6],[8,2,9,1,3,1,9,7,2,5,3,1,2,4,8,2,8,8],[6,7,9,8,4,8,3,0,4,0,9,6,6,0,0,5,1,4],[7,1,3,1,8,8,3,1,2,1,5,0,2,1,9,1,1,4],[9,5,4,3,5,6,1,3,6,4,9,7,0,8,0,3,9,9],[1,4,2,5,8,7,7,0,0,7,1,2,1,2,7,7,7,4],[3,9,7,9,5,8,9,5,6,9,8,8,0,1,4,2,8,2],[1,5,2,2,2,5,6,3,9,3,1,7,9,6,8,6,8,3],[5,7,8,3,8,8,3,9,9,8,1,9,2,5,4,7,7,7],[2,3,2,4,8,5,1,7,2,9,5,2,4,2,9,2,8,7],[0,1,6,1,1,0,0,6,5,4,3,4,3,7,9,6,1,9]]
ans5 = 85
res = su.minPathSum(grid)
assert(ans5 == res)