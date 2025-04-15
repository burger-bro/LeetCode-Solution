from typing import List

class Solution:
    def minimumCost(self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:
        # ans = float("inf")

        # def dfs(cur_cost, visited_h, visited_v, seg_h, seg_v):
        #     for i in range(m):
        #         if visited_h[i]:
        #             continue
        #         visited_h[i] = True
        #         cur_cost = dfs(visited_h, visited_v, seg_h+1, seg_v)

        horizontalCut.sort()
        verticalCut.sort()
        seg_h, seg_v = 1, 1
        cost = 0
        while horizontalCut and verticalCut:
            if horizontalCut[-1] > verticalCut[-1]:
                tmp = horizontalCut.pop()
                cost += tmp * seg_v
                seg_h += 1
            else:
                tmp = verticalCut.pop()
                cost += tmp * seg_h
                seg_v += 1
            
        while horizontalCut:
            tmp = horizontalCut.pop()
            cost += tmp * seg_v
            seg_h += 1
        while verticalCut:
            tmp = verticalCut.pop()
            cost += tmp * seg_h
            seg_v += 1
        # print(cost)
        return cost

su = Solution()
m = 3
n = 2 
horizontalCut = [1,3]
verticalCut = [5]
ans = 13
res = su.minimumCost(m, n, horizontalCut, verticalCut)
assert(res == ans)

m = 2
n = 2
horizontalCut = [7]
verticalCut = [4]
ans = 15
res = su.minimumCost(m, n, horizontalCut, verticalCut)
assert(res == ans)

# m = 5
# n = 5
# horizontalCut = [1,3,5,7,9]
# verticalCut = [2,4,6,8]
# ans = 15
# res = su.minimumCost(m, n, horizontalCut, verticalCut)
# assert(res == ans)
