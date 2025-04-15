class Solution(object):
    def numberOfSubstrings(self, s: str) -> int:
        # 注意到输入规模是10^4，因此算法至少要优于O(N^2)
        # 1.考虑暴力方法进行O(N^2)迭代，如果abc在前面已经出现，后续不用迭代，直接相加
        # 优化1:如果一轮都没有找到，则没必要进行下一轮
        # 优化2:如果是aaaaaaaa+bc这种形式如何处理？
        # 2.考虑dp方法：是否具有重叠子问题？
        ret = 0
        for i in range(len(s)):
            d = set()
            for j in range(i, len(s)):
                d.add(s[j])
                if len(d) == 3:
                    ret += len(s) - j
                    break
        print(ret)
        return ret

    def numberOfSubstrings(self, s: str) -> int:
        # 注意到输入规模是10^4，因此算法至少要优于O(N^2)
        # 1.考虑暴力方法进行O(N^2)迭代，如果abc在前面已经出现，后续不用迭代，直接相加
        # 优化1:如果一轮都没有找到，则没必要进行下一轮
        # 优化2:如果是aaaaa+bc, abcccccc, cccabcccc, abcabcabc
        # aaaaaaaaaabc: abc + num_a
        # abcabcabc: abc+len(..) bca+len(..) cab+len(..)
        # abbbbcabc: abbbbbbc+  
        # 2.考虑dp方法：是否具有重叠子问题？
        ret = 0
        for i in range(len(s)):
            d = set()
            for j in range(i, len(s)):
                d.add(s[j])
                if len(d) == 3:
                    ret += len(s) - j
                    break
            else:
                break
        print(ret)
        return ret

    def numberOfSubstrings(self, s: str) -> int:
        from collections import deque
        ret = 0 
        id_a, id_b, id_c = deque([]), deque([]), deque([])
        for i, c in enumerate(s):
            eval(rf"id_{c}").append(i)
        while id_a and id_b and id_c:
            ai, bi, ci = id_a[0], id_b[0], id_c[0]
            min_ = min(ai, bi, ci)
            max_ = max(ai, bi, ci)
            ret += len(s)-max_
            for id_x in (id_a, id_b, id_c):
                if id_x[0] == min_:
                    id_x.popleft()
                    break
            # print(ai, bi, ci, max_, min_, ret)
        print(ret)
        return ret

    def numberOfSubstrings(self, s: str) -> int:
        d = {'a':0, 'b':0, 'c':0}
        ret = 0
        left = 0
        for right in range(len(s)):
            d[s[right]] += 1
            while all(v > 0 for v in d.values()):
                ret += len(s)-right
                d[s[left]] -= 1
                left += 1
        print(ret)
        return ret

su = Solution()

# case std1
s = "abcabc"
res = su.numberOfSubstrings(s)
ans = 10
assert(res == ans)

# case std2
s = "aaacb"
res = su.numberOfSubstrings(s)
ans = 3
assert(res == ans)


# case1 
s = "abc"
res = su.numberOfSubstrings(s)
ans = 1
assert(res == ans)

# case2
s = "aaa"
res = su.numberOfSubstrings(s)
ans = 0
assert(res == ans)

# case3 perf
s = "aaaaa" * 10000 
res = su.numberOfSubstrings(s)
ans = 0
assert(res == ans)

# case4 perf
s = "abc" + "aaaaa" * 10000 
res = su.numberOfSubstrings(s)
ans = 100001
assert(res == ans)

# case5 perf
s = "aaaaa" * 10000 + "abc"
res = su.numberOfSubstrings(s)
ans = 50001
assert(res == ans)

# case6 perf
s = "abc" * 10000
res = su.numberOfSubstrings(s)
ans = 449955001
assert(res == ans)
