class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ret = 0
        mul = 1
        for c in columnTitle[::-1]:
            ret += (ord(c) - ord('A') + 1) * mul
            mul *= 26
            print(ret)
        print("ret", ret)
        return ret

su = Solution()

# case std1
columnTitle = "A"
ans = 1
res = su.titleToNumber(columnTitle)
assert(res == ans)
exit(0)

# case std2
columnTitle = "AB"
ans = 28
res = su.titleToNumber(columnTitle)
assert(res == ans)

# case std3
columnTitle = "A"
ans = 701
res = su.titleToNumber(columnTitle)
assert(res == ans)

