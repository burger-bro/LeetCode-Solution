from functools import cache

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        ans = None
        def dfs(p1, p2, p3):
            nonlocal ans
            if p3 == len(s3):
                print("what?")
                ans = True
                return
            if ans is not None or p3 > len(s3):
                return
            if p1 < len(s1) and s3[p3] == s1[p1]:
                dfs(p1+1, p2, p3+1)
            if p2 < len(s2) and s3[p3] == s2[p2]:
                dfs(p1, p2+1, p3+1)
            return
        dfs(0, 0, 0)
        # print(ans)
        return ans if ans else False


    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        @cache
        def dfs(p1, p2, p3):
            if p3 == len(s3):
                # print("what?")
                return True
            if p3 > len(s3):
                return False
            tmp1, tmp2 = False, False
            if p1 < len(s1) and s3[p3] == s1[p1]:
                tmp1 = dfs(p1+1, p2, p3+1)
            if p2 < len(s2) and s3[p3] == s2[p2]:
                tmp2 = dfs(p1, p2+1, p3+1)
            return tmp1 or tmp2
        # dfs(0, 0, 0)
        # print(ans)
        tmp_res = dfs(0, 0, 0)
        return tmp_res

    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        @cache
        def dfs(p1, p2):
            if p1 + p2 == len(s3):
                # print("what?")
                return True
            if p1 + p2 > len(s3):
                return False
            tmp1, tmp2 = False, False
            if p1 < len(s1) and s3[p1 + p2] == s1[p1]:
                tmp1 = dfs(p1+1, p2)
            if p2 < len(s2) and s3[p1 + p2] == s2[p2]:
                tmp2 = dfs(p1, p2+1)
            return tmp1 or tmp2
        # dfs(0, 0, 0)
        # print(ans)
        tmp_res = dfs(0, 0)
        return tmp_res

su = Solution()

# case std1
s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"
ans = True
res = su.isInterleave(s1, s2, s3)
assert(ans == res)

# case std2
s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbbaccc"
ans = False
res = su.isInterleave(s1, s2, s3)
assert(ans == res)


# case std3
s1 = ""
s2 = ""
s3 = ""
ans = True
res = su.isInterleave(s1, s2, s3)
assert(ans == res)

# case1 boundry min+1 pos
s1 = "a"
s2 = "c"
s3 = "ac"
ans = True
res = su.isInterleave(s1, s2, s3)
assert(ans == res)

# case2 boundry min+1 pos
s1 = "a"
s2 = "c"
s3 = "ca"
ans = True
res = su.isInterleave(s1, s2, s3)
assert(ans == res)

# case3 boundry min+1 neg
s1 = "a"
s2 = "c"
s3 = "b"
ans = False
res = su.isInterleave(s1, s2, s3)
assert(ans == res)

# case4 boundry min+1 neg
s1 = "a"
s2 = "c"
s3 = "bb"
ans = False
res = su.isInterleave(s1, s2, s3)
assert(ans == res)

# case5 boundry min+1 neg
s1 = "a"
s2 = "a"
s3 = "bb"
ans = False
res = su.isInterleave(s1, s2, s3)
assert(ans == res)

# case6 boundry min+1 pos
s1 = "a"
s2 = "a"
s3 = "aa"
ans = True
res = su.isInterleave(s1, s2, s3)
assert(ans == res)

# case7 boundry max pos
s1 = "a" * 100
s2 = "c" * 100
s3 = "ac" * 100
ans = True
res = su.isInterleave(s1, s2, s3)
assert(ans == res)

# case8 boundry max neg
s1 = "a" * 100
s2 = "c" * 100
s3 = "cb" * 100
ans = False
res = su.isInterleave(s1, s2, s3)
assert(ans == res)

# case9 s1 + s2 < s3
s1 = "a" * 200
s2 = "c" * 199
s3 = "ac" * 200
ans = False
res = su.isInterleave(s1, s2, s3)
assert(ans == res)

# case10 s1 + s2 > s3
s1 = "a" * 201
s2 = "c" * 200
s3 = "ab" * 200
ans = False
res = su.isInterleave(s1, s2, s3)
assert(ans == res)

# case10 s1 + s2 > s3 and s1 has a extra char?
s1 = "a" * 201
s2 = "c" * 200
s3 = "ac" * 200
ans = False
res = su.isInterleave(s1, s2, s3)
assert(ans == res)

# case11 aaaaabbbbbb
s1 = "aaaaa"
s2 = "bbbbb"
s3 = "aaaaabbbbb"
ans = True
res = su.isInterleave(s1, s2, s3)
assert(ans == res)

# case12 aaaaabbbbbb
s1 = "aaaaa"
s2 = "bbbbb"
s3 = "bbbbbaaaaa"
ans = True
res = su.isInterleave(s1, s2, s3)
assert(ans == res)

# case13 aaaaabbbbbb
s1 = "aaaaa"
s2 = "bbbbb"
s3 = "ababababab"
ans = True
res = su.isInterleave(s1, s2, s3)
assert(ans == res)

# case14 aaaaabbbbbb
s1 = "aaaaa"
s2 = "bbbbb"
s3 = "bababababa"
ans = True
res = su.isInterleave(s1, s2, s3)
assert(ans == res)

# case15 aaaaabbbbbb
s1 = "aaaaa"
s2 = "bbbbb"
s3 = "aabbbbbaaa"
ans = True
res = su.isInterleave(s1, s2, s3)
assert(ans == res)

# case TLE
s1 = "bbbbbabbbbabaababaaaabbababbaaabbabbaaabaaaaababbbababbbbbabbbbababbabaabababbbaabababababbbaaababaa"
s2 = "babaaaabbababbbabbbbaabaabbaabbbbaabaaabaababaaaabaaabbaaabaaaabaabaabbbbbbbbbbbabaaabbababbabbabaab"
s3 = "babbbabbbaaabbababbbbababaabbabaabaaabbbbabbbaaabbbaaaaabbbbaabbaaabababbaaaaaabababbababaababbababbbababbbbaaaabaabbabbaaaaabbabbaaaabbbaabaaabaababaababbaaabbbbbabbbbaabbabaabbbbabaaabbababbabbabbab"
su.isInterleave(s1, s2, s3)

