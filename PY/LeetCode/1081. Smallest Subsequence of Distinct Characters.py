from collections import Counter, deque
class Solution:
    def smallestSubsequence(self, s: str) -> str:
        """
        条件1：s需要包含所有元素至少一次
        条件2：字典序最小

        思路1：尽量使字典序小，同时寻找满足条件1的s（优化思路）
        思路2：列出所有满足条件1的s，找字典序最小的那一个（朴素的暴力方法）
        补充：应该可以在O(n)时间内遍历所有1
        """
        distinct_num = len(Counter(s).keys())
        print(distinct_num)
        last_non_visitd = -1
        subs = deque()
        i = 0
        smallest = "z"*distinct_num
        while i < len(s):
            print(subs, i)
            last_non_visitd = i if last_non_visitd == -1 else last_non_visitd# ?
            if len(subs) != distinct_num:
                if s[i] not in subs:
                    subs.append(s[i])
                else:
                    pass
                    # last_non_visitd = i if last_non_visitd == -1 else last_non_visitd# ?
            if len(subs) == distinct_num:
                t = "".join(subs)
                print(t)
                smallest = min(t, smallest)
                # subs.popleft()
                # i = last_non_visitd
                # last_non_visitd = -1
                subs.clear()
                i = last_non_visitd
                last_non_visitd = -1
            i += 1
        print("res:", smallest)
        return smallest

    def smallestSubsequence(self, s: str) -> str:
        d = Counter(s)
        distinct_num = len(d.keys())
        stack = [s[0]]
        d[s[0]] -= 1
        for i in range(1, len(s)):
            print(stack, d)
            if s[i] in stack or len(stack) == distinct_num:
                d[s[i]] -= 1
                continue
            while stack and s[i] < stack[-1] and d[stack[-1]] > 0:
                stack.pop()
            stack.append(s[i])

            d[s[i]] -= 1

        print("res", stack)
        return "".join(stack)
su = Solution()
# case std1
s = "bcabc"
res = su.smallestSubsequence(s)
ans = "abc"
assert(res == ans)
# case std2
s = "cbacdcbc"
res = su.smallestSubsequence(s)
ans = "acdb"
assert(res == ans)

# case1
s = "a"
res = su.smallestSubsequence(s)
ans = "a"
assert(res == ans)

# case2
s = "aa"
res = su.smallestSubsequence(s)
ans = "a"
assert(res == ans)

# case3
s = "ab"
res = su.smallestSubsequence(s)
ans = "ab"
assert(res == ans)

# case4
s = "cbabc"
res = su.smallestSubsequence(s)
ans = "abc"
assert(res == ans)

# case5
s = "bxxaxcxxxxxaxxxxx"
res = su.smallestSubsequence(s)
ans = "bacx"
assert(res == ans)

# case6
s = "axxxxbxxxxxcxxxxx"
res = su.smallestSubsequence(s)
ans = "abcx"
assert(res == ans)
