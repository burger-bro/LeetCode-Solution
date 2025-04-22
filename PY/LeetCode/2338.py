from functools import lru_cache

class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        """
        (1) 1 < a[i] < max
        (2) arr[i+1] % arr[i] == 0

        n^maxValue个可能的array

        性质：
        n n n n n n n是一个ideal array
        1 [ideal array] 是一个ideal array
        start [ideal array] 是一个ideal array
        [ideal array] end 是一个ideal array
        a ka k^2a k^3a 

        方法1:
        1
            k=1 : 1 1 1 1 1
            k=2 : 1 2 4 8 16
                : 1 2 4 8 8

                : 1 2 2 2 2
                : 1 2 4 4 4
        
        方法2:
        从maxValue反向出发 从所有最大值里面选 每个值都存储他可以整除的个数
        从1正向出发

        方法3:
        所有的值后面可以接相应的倍数，这个连接算作一条边
        """
        value_map = {}
        for i in range(1, maxValue+1):
            value_map[i] = []
            k = i + i
            while k <= min(1e4, maxValue):
                value_map[i].append(k)
                k += i

        print(value_map)

        @lru_cache(None)
        def dfs(cur_n, value):
            # print(cur_n, value)
            if cur_n == n:
                return 1 #?
            ret = 1
            for nxt_num in range(cur_n+1, n+1):
                for nxt_v in value_map[value]:
                    ret += dfs(nxt_num, nxt_v)
                    ret %= 1e9 + 7
            # print(ret)
            return ret      
        
        ret_val = 0
        for i in range(1, maxValue+1):
            ret_val += dfs(1, i)

        # print(dfs(1, 1))
        # print(dfs(1, 2))
        # print(dfs(1, 3))
        print("ret: ", ret_val)
        return ret_val


    def idealArrays(self, n: int, maxValue: int) -> int:
        value_map = {}
        for i in range(1, maxValue+1):
            value_map[i] = []
            k = i + i
            while k <= min(1e4, maxValue):
                value_map[i].append(k)
                k += i

        @lru_cache(None)
        def dfs(cur_n, value):
            if cur_n == 0:
                return 1 #?
            ret = 1
            for nxt_num in range(0, cur_n):
                for nxt_v in value_map[value]:
                    ret += dfs(nxt_num, nxt_v)
            # print("debug ret",cur_n, value, ret)
            return ret      
        
        ret_val = 0
        # for i in range(1, maxValue+1):
        #     ret_val += dfs(n-1, i)

        for i in range(maxValue, 0, -1):
            ret_val += dfs(n-1, i)

        # print(dfs(1, 1))
        # print(dfs(1, 2))
        # print(dfs(1, 3))
        print("ret: ", ret_val)
        return ret_val

    def idealArrays(self, n: int, maxValue: int) -> int:
        possible_chains = {} 



su = Solution()
# case perf
n = 380
maxValue = 194
res = su.idealArrays(n, maxValue)
ans = 10
### assert(res == ans)


# case std1
n = 2
maxValue = 5
res = su.idealArrays(n, maxValue)
ans = 10
assert(res == ans)

# case std2
"""
    {1: [2, 3], 2: [], 3: []}
    多个n的情况 在进入当前节点时 遍历重复多个n的种数
"""
n = 5
maxValue = 3
res = su.idealArrays(n, maxValue)
ans = 11
assert(res == ans)


