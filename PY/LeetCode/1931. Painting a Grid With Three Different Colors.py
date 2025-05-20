class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        start = [3*2**i for i in range(5)]
        print(start)
        start = [3, 6, 12, 24, 48]
        rate = [2, 3, 4, 7, 9]
        ret = start[m-1] * pow(rate[m-1], n-1)
        print(start[m-1], "*", pow(rate[m-1], n-1))
        print("ret", ret)
        return ret

    def help(self, num):
        # calc rate
        # ss = [['A', 'B'], ['A', 'C'], ['A', 'B'], ['B', 'C']]
        ss = [['B', 'C'], ['A', 'C'], ['A', 'B']]
        # ss = [['A', 'B'], ['A', 'C'], ['A', 'B'], ['B', 'C'], ['A', 'C']]
        candi = set()
        num = len(ss)
        def dfs(i, cur):
            if len(cur) == num:
                candi.add(cur)
                return
            if not cur:
                dfs(i+1, ss[i][0])
                dfs(i+1, ss[i][1])
                return
            cur[-1] != ss[i][0] and dfs(i+1, cur+ss[i][0])
            cur[-1] != ss[i][1] and dfs(i+1, cur+ss[i][1])
        dfs(0, "")
        print(candi)

su = Solution()
# su.help(4)
# case1
m = 1
n = 1
res = su.colorTheGrid(m, n)
ans = 3
assert(res == ans)
# case2
m = 1
n = 2
res = su.colorTheGrid(m, n)
ans = 6
assert(res == ans)
