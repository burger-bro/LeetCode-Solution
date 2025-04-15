from typing import List

class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        """
        给定k(k>=1) 将weights分割为k个区间
        cost=0+ x+(x+3) +(n-1)
        如何定义取区间分割时的度量？
        1:定义为将分割元素归到前面，后续元素归到后面
        度量计算： costi = cost(i-1) + weight[i] + weight[i+1]
        i<n-1
        2.可能存在重复选择吗？
        [1,3][5,1] idx=1已选,剩余可选0,2
        """
        if len(weights) == 1: return 0
        idx_cost = [weights[i]+weights[i+1] for i in range(len(weights)-1)]
        idx_cost.sort()
        print(idx_cost)
        print(idx_cost[len(idx_cost)-(k-1):])
        print(idx_cost[:k])
        maximum = sum(idx_cost[len(idx_cost)-(k-1):])
        minimum = sum(idx_cost[:k-1])
        print(maximum, minimum)
        ret = maximum-minimum
        print(ret)
        return ret

    def putMarbles(self, weights: List[int], k: int) -> int:
        if len(weights) == 1: return 0
        cost = sorted([weights[i]+weights[i+1] for i in range(len(weights)-1)])
        return sum(cost[-1-i]-cost[i] for i in range(k-1))

    def putMarbles(self, weights: List[int], k: int) -> int:
        return 0 if (cost:= sorted([weights[i]+weights[i+1] for i in range(len(weights)-1)])) and len(weights) == 1 else sum(cost[-1-i]-cost[i] for i in range(k-1)) 

su = Solution()
# case std3
weights = [1,4,2,5,2]
k = 3
res = su.putMarbles(weights, k)
ans = 3
assert(res == ans)


# case std1
weights = [1,3,5,1]
k = 2
res = su.putMarbles(weights, k)
ans = 4
assert(res == ans)

# case std2
weights = [1,3]
k = 2
res = su.putMarbles(weights, k)
ans = 0
assert(res == ans)

