from collections import Counter
from functools import lru_cache

class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums) -> int:
        mod = 10**9+7

        @lru_cache(None)
        def recursive(ch, n):
            tmp = ord('z') - ord(ch) + 1
            if tmp > n:
                return 1
            nxt_n = n - tmp
            sub_a = recursive('a', nxt_n) % mod
            sub_b = recursive('b', nxt_n) % mod
            return sub_a + sub_b
        
        d = Counter(s)
        ret = 0
        for k, v in d.items():
            ret += recursive(k, t) * v
            print(k, v, ret)
        
        print(ret)
        return ret


su = Solution()
# case perf
# s = "zxpoashfqwagxckbnihoqriazyoad"*3*100
# t = 5000
# res = su.lengthAfterTransformations(s, t)
# ans = 7
# assert(res == ans)

# case std1
s = "abcyy"
t = 2
nums = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2]
res = su.lengthAfterTransformations(s, t, nums)
ans = 7
assert(res == ans)
# case std2
s = "azbk"
t = 1
nums = [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]
res = su.lengthAfterTransformations(s, t, nums)
ans = 8
assert(res == ans)