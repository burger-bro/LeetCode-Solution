class Solution:
    def countSubstrings(self, s: str, c: str) -> int:
        n = s.count(c)
        return sum(i for i in range(s.count(c)+1))
        n = s.count(c)
        return ((1 + n)*n)//2

su = Solution()
s = "abada"
c = "a"
ans = 6
res = su.countSubstrings(s, c)
assert(res == ans)


s = "abbabbbabda"
c = "a"
ans = 10
res = su.countSubstrings(s, c)
assert(res == ans)
