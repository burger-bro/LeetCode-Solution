from typing import List 
from collections import deque

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def bfs(i, j):
            directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
            visited = set([(i, j)])
            queue = deque([(i, j)])
            surround_flag = True
            while queue:
                x, y = queue.popleft()
                if x == 0 or x == m-1 or y == 0 or y == n-1:
                    surround_flag = False
                for dir in directions:
                    nxt_x, nxt_y = x + dir[0], y + dir[1]
                    if 0 <= nxt_x < m and 0 <= nxt_y < n and (nxt_x, nxt_y) not in visited and board[nxt_x][nxt_y] == 'O':
                        queue.append((nxt_x, nxt_y))
                        visited.add((nxt_x, nxt_y))
            # print("visited", visited, surround_flag)
            if surround_flag:
                for i, j in visited:
                    board[i][j] = 'X'
            else:
                not_surrounded.update(visited)


        m, n = len(board), len(board[0])
        not_surrounded = set()
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O' and (i, j) not in not_surrounded:
                    bfs(i, j)
        print(board)
        return


su = Solution()
board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
su.solve(board)
ans =  [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
assert(board == ans)

board = [["X"]]
su.solve(board)
ans = [["X"]]
assert(board == ans)

board = [["O"]]
su.solve(board)
ans = [["O"]]
assert(board == ans)

board = [["O","O","O","O"],["O","O","O","O"],["O","O","O","O"],["O","O","O","O"]]
su.solve(board)
ans =  [["O","O","O","O"],["O","O","O","O"],["O","O","O","O"],["O","O","O","O"]]
assert(board == ans)

board = [["X","X","X","X"],["X","O","O","X"],["X","O","O","X"],["X","X","X","X"]]
su.solve(board)
ans =  [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","X","X","X"]]
assert(board == ans)
