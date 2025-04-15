from typing import List 
from itertools import combinations


 
def power_set(A):
    def PowerSet(A):
        if len(A) == 0:     #递归退出条件
            return [[0]]
        else:
            a = A.pop()
            # print("去除了" + a)
            p = PowerSet(A)
            for b in p:
                c = b + [a]
                p = p + [c]    #加[]是为了让c整体为一个集合元素  例{'ABC'}
            return p
    return PowerSet(A)

# print(power_set([1,5,2]))
# exit(0)

def check(A):
    if len(A) == 0:     #递归退出条件
        return 0
    a = A.pop()
    # print("去除了" + a)
    p = check(A)
    for b in p:
        c = b + a
        p = p + [c]    #加[]是为了让c整体为一个集合元素  例{'ABC'}
    return p


class Solution:
    def recoverArray(self, n: int, sums: List[int]) -> List[int]:
        """
        分析：sums排序之后，最大值一定是大于等于零的子数组之和，最小值是小于的子数组之和
        所以最大最小之和，即为要求的数组总和。
        所有的子集中，一定有一些sum就是数组元素，如何找到他们？
        如果能找到他们作为遍历的起点，则可以简化很多复杂度

        sums中2^n个子数组中，哪些是特殊的？
        (1)一个元素的子数组 (2) 大于零和小于零的子数组 (3)原数组
        他们之间有哪些关系？
        (1)大于零+小于零=原数组
        (2)从一个元素的子数组可推出其他P(2，n)个
        (3)从总数组，可以分解出单个元素和(n-1)个元素之和

        整个sums具有的性质：
        (1)存在n对: n + (N/n) = 总sum 

        方法1：任选n个数，以他们为结果，进行验证。任选的n个数之和为总数组之和时才进行验证
        """
        if len(sums) == 2:
            return [sums[0]] if not sums[1] else [sums[1]]
        sums.sort()
        print(sums)
        all_sums = sums[0] + sums[-1]
        sums.remove(0)
        sums.remove(all_sums)
        print(sums)
        visited = [False] * len(sums)
        # visited[0], visited[-1] = True, True

        possible = set()
        for i in range(len(sums)):
            for j in range(i, len(sums)):
                h = sums[j] - sums[i]
                if h in sums:
                    possible.add(h)


        def dfs(cb):
            nonlocal flag
            if not flag:
                return [0]
            if len(cb) == 0:     #递归退出条件
                return [0]
            else:
                a = cb.pop()
                # print("去除了" + a)
                p = dfs(cb)
                for b in p:
                    c = b + a
                    if c not in sums:
                        print("why?")
                        print(c, sums)
                        flag = False
                        return [0]
                    p = p + [c]    #加[]是为了让c整体为一个集合元素  例{'ABC'}
                return p
        # print("dfs")
        # print(dfs([-1,-2,3]))
        for cb in combinations(sums, n):
            continue_flag = False
            for h in cb:
                if h not in possible:
                    continue_flag = True
            if continue_flag: continue
            print(cb)
            flag = True
            dfs(list(cb))
            if flag:
                return list(cb)
        print("hey?")


su = Solution()

a = [-1,-2,3] #[1,3,4,5]
print(power_set(a))
# # case1
# n = 5
# sumss = [1,-2,4,-3,5]
# sums = power_set(sumss.copy())

# res = su.recoverArray(n, sums.copy())
# ans = sumss
# res.sort()
# ans.sort()
# print("res", res)
# print("ans", ans)
# assert(res == ans)
# exit(0)

# case1
n = 1
sums = [2, 0]
res = su.recoverArray(n, sums)
ans = [2]
assert(res == ans)

# case std1
n = 3
sums = [-3,-2,-1,0,0,1,2,3]
res = su.recoverArray(n, sums)
ans = [1,2,-3]
print("res", res)
print("ans", ans)
assert(res == ans)