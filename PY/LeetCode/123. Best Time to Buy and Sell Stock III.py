from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        variants = [prices[i]-prices[i-1] for i in range(1, len(prices))]
        print(variants)
        mem = {}
        m = len(variants)
        for i in range(m-1):
            sums = variants[i]
            for j in range(i+1, m):
                sums += variants[j]
                if sums > 0:
                    mem[(i, j)] = sums
    
    def maxProfit(self, prices: List[int]) -> int:
        print("starts")
        if len(prices) == 1: return 0

        variants = [prices[i]-prices[i-1] for i in range(1, len(prices))]
        if len(variants) == 1: return variants[0] if variants[0] > 0 else 0
        print(variants)
        m = len(prices)
        max_profits_ends_with = [0]*m
        max_profits_starts_with = [0]*m
        for i in range(1, m):
            max_profits_ends_with[i] = max(variants[i-1], variants[i-1]+max_profits_ends_with[i-1])
        max_profits_ends_with.pop(0)
        print(max_profits_ends_with)
        for i in range(m-2, -1, -1):
            max_profits_starts_with[i] = max(variants[i], variants[i]+max_profits_starts_with[i+1])
        max_profits_starts_with.pop()
        print(max_profits_starts_with)

        for i in range(1, len(variants)):
            max_profits_ends_with[i] = max(max_profits_ends_with[i-1], max_profits_ends_with[i])

        for i in range(len(variants)-2, -1, -1):
            max_profits_starts_with[i] = max(max_profits_starts_with[i+1], max_profits_starts_with[i])
  
        print(max_profits_ends_with)
        print(max_profits_starts_with)
        ret = 0
        
        for i in range(0, len(variants)-1):
            ret = max(ret, max_profits_ends_with[i]+max_profits_starts_with[i+1])
        print(ret)
        return max([ret, max_profits_ends_with[m-2], max_profits_starts_with[0]])
    

su = Solution()

# case std1
prices = [3,3,5,0,0,3,1,4]
ans = 6
res = su.maxProfit(prices)
assert(res == ans)

# case std2
prices = [1,2,3,4,5]
ans = 4
res = su.maxProfit(prices)
assert(res == ans)

# case std3
prices = [7,6,4,3,1]
ans = 0
res = su.maxProfit(prices)
assert(res == ans)

# # case1 perf
# prices = [i for i in range(100000)]
# ans = 0
# res = su.maxProfit(prices)
# # assert(res == ans)

# case2 min
prices = [1]
ans = 0
res = su.maxProfit(prices)
assert(res == ans)

# case3 2buy
prices = [1,2]
ans = 1
res = su.maxProfit(prices)
assert(res == ans)

# case3 2buy
prices = [1,3,2]
ans = 2
res = su.maxProfit(prices)
assert(res == ans)

# case4 bug
prices = [2,1,4]
ans = 3
res = su.maxProfit(prices)
assert(res == ans)