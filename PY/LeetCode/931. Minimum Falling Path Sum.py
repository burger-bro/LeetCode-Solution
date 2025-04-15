from functools import cache, lru_cache
class Solution(object):
    def minFallingPathSum(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        @cache
        def dfs(n, m):
            m = max(0, m)
            m = min(len(matrix)-1, m)
            if n == len(matrix)-1: return matrix[n][m]
            tt = matrix[n][m] + min([dfs(n+1, m+1), dfs(n+1, m), dfs(n+1, m-1)])
            return tt
        rr = min(dfs(0, i) for i in range(len(matrix)))
        print(rr)
        return rr

    def minFallingPathSum(self, matrix):
        m = len(matrix)
        dp = [[0]*m for _ in range(m)]

        for i in range(m):
            dp[0][i] = matrix[0][i]
        
        for i in range(1, m):
            for j in range(m):
                left = max(j-1, 0)
                right = min(j+1, m-1)
                dp[i][j] = matrix[i][j] + min(dp[i-1][j], dp[i-1][left], dp[i-1][right])

        return min(dp[-1])

su = Solution()
# case bug
matrix = [[100,-42,-46,-41],
          [31,97,10,-10],
          [-58,-51,82,89],
          [51,81,69,-51]]
res = su.minFallingPathSum(matrix)
ans = -36
assert(res == ans)

# case std1
matrix = [[2,1,3],[6,5,4],[7,8,9]]
res = su.minFallingPathSum(matrix)
ans = 13
assert(res == ans)

# case std1
matrix = [[2]]
res = su.minFallingPathSum(matrix)
ans = 2
assert(res == ans)

# case perf
matrix = [[2]*100 for _ in range(100)]
res = su.minFallingPathSum(matrix)
ans = 200
assert(res == ans)
