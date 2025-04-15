from typing import List

class Solution:
    def canMakeSquare(self, grid: List[List[str]]) -> bool:
        four_point = ((0, 0), (0, 1), (1,0), (1, 1))
        for i in range(len(grid) - 1):
            for j in range(len(grid) - 1):
                cnt = 0
                for p in four_point:
                    if grid[i+p[0]][j+p[1]] == "W":
                        cnt += 1
                if cnt != 2:
                    return True
        return False


su = Solution()
grid = [["B","W","B"],["B","W","W"],["B","W","B"]]
ans = True
res = su.canMakeSquare(grid)
assert(res == ans)

grid = [["B","B","B"],["B","B","B"],["B","B","B"]]
ans = True
res = su.canMakeSquare(grid)
assert(res == ans)

grid = [["B","B","B"],["W","W","W"],["B","B","B"]]
ans = False
res = su.canMakeSquare(grid)
assert(res == ans)
