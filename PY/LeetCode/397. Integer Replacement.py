from functools import cache
class Solution:
    @cache
    def integerReplacement(self, n: int) -> int:
        if n == 1:
            return 0
        if n % 2 == 0:
            return 1 + self.integerReplacement(n//2)
        else:
            return 1 + min(self.integerReplacement(n+1), self.integerReplacement(n-1))

su = Solution()
# case std1
n = 8
res = su.integerReplacement(n)
ans = 3
print(res)
assert(res == ans)
# case std2
n = 7
res = su.integerReplacement(n)
ans = 4
assert(res == ans)
# case std3
n = 4
res = su.integerReplacement(n)
ans = 2
assert(res == ans)

# case min
n = 1
res = su.integerReplacement(n)
ans = 0
assert(res == ans)

# case perf
n = 1000000000007
res = su.integerReplacement(n)
ans = 2
print("end", res)
# assert(res == ans)

