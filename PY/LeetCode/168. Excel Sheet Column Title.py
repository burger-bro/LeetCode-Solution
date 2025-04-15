class Solution(object):
    def convertToTitle(self, columnNumber):
        columnNumber = 1456
        denominator = 26
        ans = ''
        while columnNumber:
            div_, mod_ = divmod(columnNumber-1, denominator)
            ans = chr(ord('A')+mod_) + ans
            # ans = str(mod_) + ans
            columnNumber = div_
        print(ans)
        return ans



su = Solution()

# case1
columnNumber = 2147483647
ans = "A"
res = su.convertToTitle(columnNumber)
# assert(res == ans)
exit(0)

# case std1
columnNumber = 1
ans = "A"
res = su.convertToTitle(columnNumber)
assert(res == ans)
# exit(0)

# case std2
columnNumber = 28
ans = "AB"
res = su.convertToTitle(columnNumber)
assert(res == ans)

# case std3
columnNumber = 701
ans = "ZY"
res = su.convertToTitle(columnNumber)
assert(res == ans)
