from typing import List
import random
import threading
import heapq

class Solution:
    def minTimeToReach0(self, moveTime: List[List[int]]) -> int:
        n, m = len(moveTime), len(moveTime[0])
        direction = ((0, -1), (-1, 0), (1, 0), (0, 1))
        visited_array = [[True] * m for _ in range(n)]
        ret = float("inf")
        def dfs(room, visited, sec, flip):
            nonlocal ret
            if sec > ret:
                return
            if room[0] == n - 1 and room[1] == m - 1:
                ret = min(ret, sec)
                return
            for d in direction:
                n_r = (room[0] + d[0], room[1] + d[1])
                if 0 <= n_r[0] < n and 0 <= n_r[1] < m and visited[n_r[0]][n_r[1]]:
                    visited[n_r[0]][n_r[1]] = False
                    dfs(n_r, visited, max(sec, moveTime[n_r[0]][n_r[1]])+(1 if flip else 2), not flip)
                    visited[n_r[0]][n_r[1]] = True

        dfs((0, 0), visited_array, 0, True)
        print(ret)
        return ret

    def minTimeToReach1(self, moveTime: List[List[int]]) -> int:
        n, m = len(moveTime), len(moveTime[0])
        direction = ((0, -1), (-1, 0), (1, 0), (0, 1))
        ret = float("inf")
        dp = [[None]*m for _ in range(n)]
        dp[0][0] = (moveTime[0][0], True)
        visited_array = [[True] * m for _ in range(n)]
        def recurse(room):
            # print(room, dp)

            # if dp[room[0]][room[1]] == "working":
            #     return float("inf"), True
            # dp[room[0]][room[1]] = "working"
            if not visited_array[room[0]][room[1]]:
                # visited_array[room[0]][room[1]] = False
                return float("inf"), True
            
            if room[0] == room[1] == 0:
                return moveTime[0][0], True
            
            last_rooms = []
            for d in direction:
                n_r = (room[0] + d[0], room[1] + d[1])
                if 0 <= n_r[0] < n and 0 <= n_r[1] < m:
                    if dp[n_r[0]][n_r[1]] is None:
                        visited_array[room[0]][room[1]] = False
                        tmp_ans = recurse((n_r[0], n_r[1]))
                        dp[n_r[0]][n_r[1]] = tmp_ans
                        visited_array[room[0]][room[1]] = True
                    else:
                        tmp_ans = dp[n_r[0]][n_r[1]]
                    last_rooms.append(tmp_ans)

            last_rooms.sort(key=lambda x: (x[0], x[1]))  # may cause bug 470 True(+2) and 471 False(+1)?
            new_ans = (max(last_rooms[0][0], moveTime[room[0]][room[1]]) + (1 if last_rooms[0][1] else 2), not last_rooms[0][1])
            dp[room[0]][room[1]] = new_ans
            return new_ans
        
        ret, _ = recurse((n-1, m-1))
        print(dp)
        print(ret)
        return ret

    # def minTimeToReach(self, moveTime: List[List[int]]) -> int:
    #     n, m = len(moveTime), len(moveTime[0])
    #     direction = ((0, -1), (-1, 0), (1, 0), (0, 1))
    #     ret = float("inf")

    #     dp = [[None]*m for _ in range(n)]
    #     dp[0][0] = (moveTime[0][0], True)
    #     def recurse(room): 
    #         if room[0] == room[1] == 0:
    #             return moveTime[0][0], True
            
    #         last_rooms = []
    #         for d in direction:
    #             n_r = (room[0] + d[0], room[1] + d[1])
    #             if 0 <= n_r[0] < n and 0 <= n_r[1] < m:
    #                 if dp[n_r[0]][n_r[1]] is None:
    #                     tmp_ans = recurse((n_r[0], n_r[1]))
    #                     dp[n_r[0]][n_r[1]] = tmp_ans
    #                 else:
    #                     tmp_ans = dp[n_r[0]][n_r[1]]
    #                 last_rooms.append(tmp_ans)

    #         last_rooms.sort(key=lambda x: (x[0], x[1]))  # may cause bug 470 True(+2) and 471 False(+1)?
    #         new_ans = (max(last_rooms[0][0], moveTime[room[0]][room[1]]) + (1 if last_rooms[0][1] else 2), not last_rooms[0][1])
    #         dp[room[0]][room[1]] = new_ans
    #         return new_ans
        
    #     ret, _ = recurse((n-1, m-1))

    #     print(dp)
    #     print(ret)
    #     return ret


    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n, m = len(moveTime), len(moveTime[0])
        dp = [[float("inf")] * m for _ in range(n)]
        dp[0][0] = 0
        directions = ((0, -1), (-1, 0), (1, 0), (0, 1))
        queue = [(0, (0, 0), 1)]
        while queue:
            c_cost, c_pos, c_flag = heapq.heappop(queue)
            c_n, c_m = c_pos
            # print(c_cost, c_n, c_m, c_cost)
            for d in directions:
                n_n, n_m = c_n+d[0], c_m+d[1]
                if 0 <= n_n < n and 0 <= n_m < m:
                    n_cost = max(c_cost, moveTime[n_n][n_m]) + c_flag
                    if n_cost < dp[n_n][n_m]:
                        n_q = (n_cost, (n_n, n_m), 2 if c_flag == 1 else 1)
                        heapq.heappush(queue, n_q)
                        dp[n_n][n_m] = n_cost
            
        # print(dp)
        # print(dp[n-1][m-1])
        return dp[n-1][m-1]

su = Solution()
moveTime = [[0,4],[4,4]]
ans = 7
res = su.minTimeToReach(moveTime)
assert(ans == res)

moveTime = [[0,0,0,0],[0,0,0,0]]
ans = 6
res = su.minTimeToReach(moveTime)
assert(ans == res)

moveTime = [[0,1],[1,2]]
ans = 4
res = su.minTimeToReach(moveTime)
assert(ans == res)      

# snake case1
moveTime = [[0,999,999,999,999],[0,999,0,0,0],[0,999,0,999,0],[0,0,0,999,0]]

# [[(0, True), (1000, False), (inf, False), (inf, True), (inf, False)]
#  [(1, False), (1002, True), (inf, True), (inf, False), (inf, True)]
#  [(3, True), (inf, False), (inf, True), (inf, True), (inf, False)]
#  [(4, False), (6, True), (7, False), (1001, True), (1002, False)]]

ans = 16
res = su.minTimeToReach(moveTime)
assert(ans == res)   

# snake case2
moveTime = [[0,1,1,1,1],[0,999,0,0,0],[0,999,0,999,0],[0,0,0,999,0]]
ans = 11
res = su.minTimeToReach(moveTime)
assert(ans == res) 

### performance case 
print("start")
moveTime = [[random.randint(0, 10) for _ in range(20)] for _ in range(20)]
res = su.minTimeToReach(moveTime)
print("finish")

