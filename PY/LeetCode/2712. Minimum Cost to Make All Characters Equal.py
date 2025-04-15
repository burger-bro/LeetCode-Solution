

class Solution:
    # def minimumCost(self, s: str) -> int:
    #     def recursive(s, ch):
    #         if len(s) == 1:
    #             return 0 if s[0] == ch else 1
    #         if len(s) <= 0:
    #             return 0
    #         min_res = float("inf")
    #         for i in range(len(s)):
    #             min_res = min(recursive(s[:i], s[i]) + recursive(s[i+1:], s[i]), min_res)
    #             print(s, i, s[:i], s[i+1:], min_res)
    #         return min_res
    #     return min(recursive(s, '0'), recursive(s, '1'))

    def minimumCost(self, s: str) -> int:
        if len(s) == 1: return 0

        min_res = float("inf")

        prefix = [0] * (len(s))
        prefix[1] = 0 if s[0] == s[1] else 1 
        for i in range(2, len(s)):
            prefix[i] = prefix[i-1] + (0 if s[i-1] == s[i] else i)
        # print(prefix)

        suffix = [0] * (len(s))
        suffix[-2] = 0 if s[-1] == s[-2] else 1 
        for i in range(len(s)-3, -1, -1):
            suffix[i] = suffix[i+1] + (0 if s[i+1] == s[i] else (len(s) - i - 1))
        # print(suffix)

        for i in range(len(s)):
            min_res = min(prefix[i] + suffix[i], min_res)
        # print(min_res)

        return min_res

    def minimumCost(self, s: str) -> int:
        return sum(min(i,len(s)-i) for i in range(1,len(s)) if s[i]!=s[i-1])


su = Solution()
s = "0011"
ans = 2
res = su.minimumCost(s)
print(res)
assert(res == ans)

s = "010101"
ans = 9
res = su.minimumCost(s)
print(res)
assert(res == ans)

s = "0"
ans = 0
res = su.minimumCost(s)
print(res)
assert(res == ans)

s = "01"
ans = 1
res = su.minimumCost(s)
print(res)
assert(res == ans)

s = "00"
ans = 0
res = su.minimumCost(s)
print(res)
assert(res == ans)

# "010101"
# "001010" 5
# "000101" 4
# "000101" 3 
# "000010" 2
# "000001" 1
# "000000" 
# "0001" 
