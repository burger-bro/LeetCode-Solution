from collections import Counter
from functools import cache

class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        # 如果字符串对应的一部分是完全相同的，则可以忽略这一部分，去替换其他的
        # 如果字符串对应的一部分字符相同，顺序不同，则可以对换。否则结束
        # abcdefg   adbecfg
        # a dbecfg    
        # a becfg d
        # 遍历子分开的子数组时，分别用两个set维护s1和s2中的字符，相等时才可以继续递归
        s1_trans_list = list(s1)
        print("******************case start******************")
        def dfs(start, end):
            nonlocal s1_trans_list, s2
            print("normal", start, end)
            if end - start <= 1:
                return True
            s1_dict1, s2_dict1 = Counter(s1_trans_list[start:end]), Counter(s2[start:end])
            s1_dict2, s2_dict2 = {}, {}
            for i in range(start, end-1):
                # print(s1_trans_list, len(s1_trans_list), i)
                print(s1_dict1, s1_dict2, s2_dict1, s2_dict2)
                s1_dict1[s1_trans_list[i]] -= 1
                try:
                    s2_dict1[s2[i]] -= 1
                except:
                    print("except")
                    return False
                s1_dict2[s1_trans_list[i]] = s1_dict2.get(s1_trans_list[i], 0) + 1
                s2_dict2[s2[i]] = s2_dict2.get(s2[i], 0) + 1
                if s1_dict1 == s2_dict1 and s1_dict2 == s2_dict2:
                    print("valid case")
                    print(s1_dict1, s1_dict2, s2_dict1, s2_dict2)
                    print("valid case")
                    tmp_ret = dfs(start, i) and dfs(i+1, end)
                    if tmp_ret:
                        return True
            
            print("reversed", start, end)
            tmp_s2 = s2[::-1]
            s1_dict1, s2_dict1 = Counter(s1_trans_list[start:end]), Counter(s2[start:end])
            s1_dict2, s2_dict2 = {}, {}
            for i in range(start, end):
                # print(s1_trans_list, len(s1_trans_list), i)
                print(s1_dict1, s1_dict2, s2_dict1, s2_dict2)
                s1_dict1[s1_trans_list[i]] -= 1
                try:
                    print('idx', end+1-i)
                    s2_dict1[s2[end+1-i]] -= 1
                except:
                    print("except")
                    return False
                s1_dict2[s1_trans_list[i]] = s1_dict2.get(s1_trans_list[i], 0) + 1
                s2_dict2[s2[end+1-i]] = s2_dict2.get(s2[end+1-i], 0) + 1
                if s1_dict1 == s2_dict1 and s1_dict2 == s2_dict2:
                    s1_bak = s1_trans_list.copy()

                    print("valid case")
                    print(s1_dict1, s1_dict2, s2_dict1, s2_dict2)
                    print("valid case")
                    s1_trans_list = s1_trans_list[i:] + s1_trans_list[:i]
                    tmp_ret = dfs(start, i) and dfs(i+1, end)
                    if tmp_ret:
                        return True
                    s1_trans_list = s1_bak


            return False
        ret = dfs(0, len(s1))
        return ret

    def isScramble(self, s1: str, s2: str) -> bool:

        # 如果字符串对应的一部分是完全相同的，则可以忽略这一部分，去替换其他的
        # 如果字符串对应的一部分字符相同，顺序不同，则可以对换。否则结束
        # abcdefg   adbecfg
        # a dbecfg    
        # a becfg d
        # 遍历子分开的子数组时，分别用两个set维护s1和s2中的字符，相等时才可以继续递归
        print("******************case start******************")
        @cache
        def dfs(sub1, sub2):
            # print(sub1, sub2)
            if len(sub1) <= 1:
                return True if sub1 == sub2 else False
            s1_dict1, s2_dict1 = Counter(sub1), Counter(sub2)
            s1_dict2, s2_dict2 = {}, {}
            if s1_dict1 != s2_dict1:
                return False
            for i in range(len(sub1)-1):
                s1_dict1[sub1[i]] -= 1
                try:
                    s2_dict1[sub2[i]] -= 1
                except:
                    print("except")
                    return False
                s1_dict2[sub1[i]] = s1_dict2.get(sub1[i], 0) + 1
                s2_dict2[sub2[i]] = s2_dict2.get(sub2[i], 0) + 1
                if s1_dict1 == s2_dict1 and s1_dict2 == s2_dict2:
                    print("valid")
                    tmp_ret = dfs(sub1[:i+1], sub2[:i+1]) and dfs(sub1[i+1:], sub2[i+1:])
                    if tmp_ret:
                        return True
            
            # print("reversed")
            sub2 = sub2[::-1]
            s1_dict1, s2_dict1 = Counter(sub1), Counter(sub2)
            s1_dict2, s2_dict2 = {}, {}
            for i in range(len(sub1)-1):
                s1_dict1[sub1[i]] -= 1
                try:
                    s2_dict1[sub2[i]] -= 1
                except:
                    print("except")
                    return False
                s1_dict2[sub1[i]] = s1_dict2.get(sub1[i], 0) + 1
                s2_dict2[sub2[i]] = s2_dict2.get(sub2[i], 0) + 1
                if s1_dict1 == s2_dict1 and s1_dict2 == s2_dict2:
                    print("valid")
                    tmp_ret = dfs(sub1[:i+1], sub2[:i+1]) and dfs(sub1[i+1:], sub2[i+1:])
                    if tmp_ret:
                        return True
            return False
        
        ret = dfs(s1, s2)
        return ret

    def isScramble(self, s1: str, s2: str) -> bool:

        # 如果字符串对应的一部分是完全相同的，则可以忽略这一部分，去替换其他的
        # 如果字符串对应的一部分字符相同，顺序不同，则可以对换。否则结束
        # abcdefg   adbecfg
        # a dbecfg    
        # a becfg d
        # 遍历子分开的子数组时，分别用两个set维护s1和s2中的字符，相等时才可以继续递归
        print("******************case start******************")
        @cache
        def dfs(sub1, sub2):
            # print(sub1, sub2)
            def helper(sub1, sub2):
                if len(sub1) <= 1:
                    return True if sub1 == sub2 else False
                s1_dict1, s2_dict1 = Counter(sub1), Counter(sub2)
                s1_dict2, s2_dict2 = {}, {}
                if s1_dict1 != s2_dict1:
                    return False
                for i in range(len(sub1)-1):
                    s1_dict1[sub1[i]] -= 1
                    try:
                        s2_dict1[sub2[i]] -= 1
                    except:
                        print("except")
                        return False
                    s1_dict2[sub1[i]] = s1_dict2.get(sub1[i], 0) + 1
                    s2_dict2[sub2[i]] = s2_dict2.get(sub2[i], 0) + 1
                    if s1_dict1 == s2_dict1 and s1_dict2 == s2_dict2:
                        print("valid")
                        tmp_ret = dfs(sub1[:i+1], sub2[:i+1]) and dfs(sub1[i+1:], sub2[i+1:])
                        if tmp_ret:
                            return True
                return False
            
            return helper(sub1, sub2) or helper(sub1, sub2[::-1])
        
        ret = dfs(s1, s2)
        return ret

# 2->4   3->3   4->2

su = Solution()

# case std1
s1 = "great"
s2 = "rgeat"
ans = True
res = su.isScramble(s1, s2)
assert(res == ans)

# case std2
s1 = "abcde"
s2 = "caebd"
ans = False
res = su.isScramble(s1, s2)
assert(res == ans)

# case std3
s1 = "a"
s2 = "a"
ans = True
res = su.isScramble(s1, s2)
assert(res == ans)

# case0 debug0
s1 = "great"
s2 = "taerg" #"rgtae"
ans = True
res = su.isScramble(s1, s2)
assert(res == ans)
# exit(0)

# case0 debug1
s1 = "great"
s2 = "rgtae" 
ans = True
res = su.isScramble(s1, s2)
assert(res == ans)
# exit(0)

# case1 boundery min  #测试用例设计时考虑正负
s1 = "b"
s2 = "b"
ans = True
res = su.isScramble(s1, s2)
assert(res == ans)

# case1 boundery min false  #测试用例设计时考虑正负
s1 = "a"
s2 = "b"
ans = False
res = su.isScramble(s1, s2)
assert(res == ans)

# case2 boundery min+1
s1 = "bc"
s2 = "cb"
ans = True
res = su.isScramble(s1, s2)
assert(res == ans)

# case3 boundery max
s1 = "".join(chr(ch) for ch in range(ord('a'), ord('z')+1)) + "bbbb"
s2 = "bbbb" + "".join(chr(ch) for ch in range(ord('a'), ord('z')+1))
ans = True
res = su.isScramble(s1, s2)
print(res)
assert(res == ans)

# case4 boundery max-1
s1 = "".join(chr(ch) for ch in range(ord('a'), ord('z')+1)) + "bbb"
s2 = "bbb" + "".join(chr(ch) for ch in range(ord('a'), ord('z')+1))
ans = True
res = su.isScramble(s1, s2)
assert(res == ans)

# case5 catrgory
s1 = "abbbbbbbbcde"
s2 = "cdeabbbbbbbb"
ans = True
res = su.isScramble(s1, s2)
assert(res == ans)

# case6 catrgory False
s1 = "abbbbbbbbcdef"
s2 = "cdeabbbbbbbbg"
ans = False
res = su.isScramble(s1, s2)
assert(res == ans)

# case7 catrgory
s1 = "abbbbbbbb"
s2 = "bbbbbbbba"
ans = True
res = su.isScramble(s1, s2)
assert(res == ans)

# case8 catrgory
s1 = "aabbbbbbbb"
s2 = "bbbbbbbbaa"
ans = True
res = su.isScramble(s1, s2)
assert(res == ans)

# case9 catrgory
s1 = "eebaacbcbcadaaedceaaacadccd"
s2 = "eadcaacabaddaceacbceaabeccd"
ans = False
res = su.isScramble(s1, s2)
assert(res == ans)


# case9 catrgory
s1 = "eebbcbcaaedceaaacad"
s2 = "eadcabadceacbceaabe"
ans = True
res = su.isScramble(s1, s2)
assert(res == ans)