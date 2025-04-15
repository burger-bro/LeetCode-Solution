from typing import List
from functools import lru_cache
from line_profiler import profile

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        """
        选择一系列question使得points最大, 但选择之间需满足bp的约束
        1:反向遍历question 依次拿题 然后判断下一个题是否能拿。这个做法似乎和直接从前面拿没什么区别，
        因为没有考虑跳过某些q不拿 而拿后面更高的
        2:按p的大小排序 优先拿最大的 拿了之后将受约束的置为invalid 再拿次大的
        不能处理case1  思考:只考虑p的收益而没考虑bp的潜在亏损 能否考虑将亏损也加入度量
        3:当看到每一个q时 如何判断是跳过还是拿
        """
        # @lru_cache(None)
        dp = [None] * len(questions)
        # @lru_cache(None)
        @profile
        def dfs(cur):
            # print(cur)
            if cur >= len(questions):
                return 0
            if dp[cur] is not None: return dp[cur]
            max_points = 0
            # for i in range(cur, len(questions)):
            #     max_points = max(max_points, questions[i][0]+dfs(i+questions[i][1]+1))
            for i in range(len(questions)-1, cur-1, -1):
                max_points = max(max_points, questions[i][0]+dfs(i+questions[i][1]+1))
            dp[cur] = max_points
            return max_points

        ret = dfs(0)
        print(ret)
        return ret


    def mostPoints(self, questions: List[List[int]]) -> int:
        dp = [0] * (len(questions))
        dp[len(questions)-1] = questions[len(questions)-1][0]
        idx = len(questions)-2
        while idx >= 0:
            dp[idx] = max(questions[idx][0], dp[idx+1])
            if idx+questions[idx][1]+1 < len(questions):
                dp[idx] = max(questions[idx][0]+dp[idx+questions[idx][1]+1], dp[idx+1])
            idx -= 1
        # print(dp)
        return dp[0]

    def mostPoints(self, questions: List[List[int]]) -> int:
        length = len(questions)
        dp = [0] * length
        dp[-1] = questions[-1][0]
        for i in range(length-2, -1, -1):
            nxt_i = i+questions[i][1]+1
            if nxt_i < length:
                dp[i] = max(questions[i][0]+dp[nxt_i], dp[i+1])
            else:
                dp[i] = max(questions[i][0], dp[i+1])
        return dp[0]

su = Solution()
# case std1
questions = [[3,2],[4,3],[4,4],[2,5]]
res = su.mostPoints(questions)
ans = 5
assert(res == ans)

# case std2
questions = [[1,1],[2,2],[3,3],[4,4],[5,5]]
res = su.mostPoints(questions)
ans = 7
assert(res == ans)

# case1
questions = [[1,5]]
res = su.mostPoints(questions)
ans = 1
assert(res == ans)

# case2
questions = [[999,1],[10000,0]]
res = su.mostPoints(questions)
ans = 10000
assert(res == ans)

# case perf
questions = [[i, i+1] for i in range(1, 5000)]
res = su.mostPoints(questions)
# ans = 10000
# assert(res == ans)
print("end")