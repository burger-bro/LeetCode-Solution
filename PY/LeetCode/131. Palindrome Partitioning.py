from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # 显然s拆分为单字符后是一个解
        # 1如果尝试从单字符开始，合并其中某一些字符，使之为回文串，就可得到另一些解
        # 比如 ababa -> (a b a b a) -> 找回文子串(aba) xx x(bab)x xx(aba) -> 
        # 如果定义一个二维数组用于记录(i,j)有几个回文子串：(0,2):{'aba', 'a b a'}
        # aaacc -> (a a a c c) -> (aaa)xx (aa)xxx x(aa)xxx -> (0,2):{'aaa'}

        # 2如果尝试从s出发开始分解呢？是否存在重叠子问题？
        # 关键在于从s出发的一级分解是否唯一
        # 比如 abaaba -> (aba aba) ()
        # 比如 ababa -> (aba b a) (a bab a) (a b aba) -> (a b a b a) (a b a b a)
        # 每一级分解较困难、不具备唯一性

        ans_set = []

        def is_palindrome(s):
            b, e = 0, len(s)-1
            while b <= e:
                if s[b] != s[e]:
                    return False
                b += 1
                e -= 1
            return True
        
        def dfs(idx, curr):
            if idx >= len(s):
                ans_set.append(curr.copy())
                return
            for i in range(idx+1, len(s)+1):
                if is_palindrome(s[idx:i]):
                    curr.append(s[idx:i])
                    dfs(i, curr)
                    curr.pop()
        dfs(0, [])
        # print(ans_set)
        return ans_set

    def partition(self, s: str) -> List[List[str]]:
        ans_set = []

        def is_palindrome(s):
            b, e = 0, len(s)-1
            while b <= e:
                if s[b] != s[e]:
                    return False
                b += 1
                e -= 1
            return True
        
        idx_pali_set = set()
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                if is_palindrome(s[i:j]):
                    idx_pali_set.add((i, j))
        print(idx_pali_set)
        
        idx_set_dict = dict()
        for se in idx_pali_set:
            if se[0] not in idx_set_dict:
                idx_set_dict[se[0]] = [se]
            else:
                idx_set_dict[se[0]].append(se)
        print(idx_set_dict)

        def dfs(level, curr):
            if level >= len(s):
                ans_set.append([s[i:j] for i, j in curr])
                return
            for se in idx_set_dict[level]:
                curr.append(se)
                dfs(se[1], curr)
                curr.pop()

        dfs(0, [])
        print(ans_set)
        return ans_set

    def partition(self, s: str) -> List[List[str]]:
        if not s: return [[]]
        ans = []
        for i in range(1, len(s)+1):
            if s[:i] == s[:i][::-1]:
                for suf in self.partition(s[i:]):
                    ans.append([s[:i]] + suf)
        print(ans)
        return ans


su = Solution()

s = "aab"
ans = [["a","a","b"],["aa","b"]]
res = su.partition(s)
assert(res == ans)

s = "a"
ans = [["a"]]
res = su.partition(s)
assert(res == ans)

s = "aa"
ans = [["a", "a"], ["aa"]]
res = su.partition(s)
assert(res == ans)

s = "aaa"
ans = [["a", "a", "a"], ["a", "aa"], ["aa", "a"],["aaa"]]
res = su.partition(s)
assert(res == ans)

s = "aabccdeqdqwewrrf"
ans = [["a","a","b"],["aa","b"]]
res = su.partition(s)

