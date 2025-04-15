class Solution:
    def arrangeCoins(self, n: int) -> int:
        cnt = 1
        while n >= cnt:
            n -= cnt
            cnt += 1
            print(cnt, n)
        print(cnt)

        (1 + r) * r * 0.5 = n
        return cnt-1

su = Solution()

# case std1
n = 5
res = su.arrangeCoins(n)
ans = 2
assert(res == ans)

# case std2
n = 8
res = su.arrangeCoins(n)
ans = 3
assert(res == ans)

# case1
n = 1
res = su.arrangeCoins(n)
ans = 1
assert(res == ans)
