from functools import cache, lru_cache

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        cnt = 0
        def dfs(si, ti):
            nonlocal cnt
            if ti == len(t):
                cnt += 1
                return
            if si == len(s):
                return
            for i in range(si, len(s)):
                if s[i] == t[ti]:
                    dfs(i+1, ti+1)
        dfs(0, 0)
        print(cnt)
        return cnt

    def numDistinct(self, s: str, t: str) -> int:
        cnt = 0
        last_valid_flag = False
        def dfs(si, ti):
            nonlocal cnt
            nonlocal last_valid_flag
            if ti == len(t):
                cnt += 1
                last_valid_flag = True
                return
            if si == len(s):
                last_valid_flag = False
                return
            for i in range(si, len(s)):
                if s[i] == t[ti]:
                    if i > si and s[i] == s[i-1] and last_valid_flag:
                        cnt += 1
                        continue
                    dfs(i+1, ti+1)
        dfs(0, 0)
        print(cnt)
        return cnt

    def numDistinct(self, s: str, t: str) -> int:
        cnt = 0
        # @lru_cache(maxsize=10000)
        def dfs(si, ti):
            if ti == len(t):
                return 1
            if si == len(s):
                return 0
            if dp[si][ti] != -1:
                return dp[si][ti]
            if s[si] == t[ti]:
                dp[si][ti] = dfs(si+1, ti+1) + dfs(si+1, ti)
                return dp[si][ti]
            else:
                dp[si][ti] = dfs(si+1, ti)
                return dp[si][ti]
        dp = [[-1 for _ in range(len(t))] for _ in range(len(s))]    
        

        cnt = dfs(0, 0)
        print(cnt)
        return cnt          
                
                

su = Solution()

# case std1
s = "rabbbit"
t = "rabbit"
ans = 3
res = su.numDistinct(s, t)
assert(res == ans)

# case std2
s = "babgbag"
t = "bag"
ans = 5
res = su.numDistinct(s, t)
assert(res == ans)

# case1 s < t p
s = "a"
t = "bag"
ans = 0
res = su.numDistinct(s, t)
assert(res == ans)

# case2 s == t n
s = "aaa"
t = "bbb"
ans = 0
res = su.numDistinct(s, t)
assert(res == ans)

# case3 s == t p
s = "aaa"
t = "aaa"
ans = 1
res = su.numDistinct(s, t)
assert(res == ans)

# case4 s > t p
s = "aaa"
t = "a"
ans = 3
res = su.numDistinct(s, t)
assert(res == ans)

# case5 s > t n
s = "aaa"
t = "b"
ans = 0
res = su.numDistinct(s, t)
assert(res == ans)

# case6 perf
s = "r"*100 + "a"*100 + "b"*200 + "i"*100 + "t"*100
t = "rabbit"
ans = 0
res = su.numDistinct(s, t)

# case7 perf2
s = "rabbit"*150
t = "rabbit"
ans = 0
res = su.numDistinct(s, t)