from typing import List

class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        position_dict = {}
        odd_cnt = 0
        for p in position:
            position_dict[p] = position_dict.get(p, 0) + 1
            if p % 2 == 0:
                odd_cnt += 1
        odd_flag = 1 if (len(position) - odd_cnt) < odd_cnt else 0
        res = 0
        # print(position_dict)
        for k, v in position_dict.items():
            if k % 2 == odd_flag:
                res += v
        # print(res)
        return res

    def minCostToMoveChips(self, position: List[int]) -> int:
        position_dict = {}
        odd_cnt = 0
        for p in position:
            position_dict[p] = position_dict.get(p, 0) + 1
            if p % 2 == 0:
                odd_cnt += 1
        return min(len(position) - odd_cnt, odd_cnt)

su = Solution()
position = [1,2,3]
ans = 1
res = su.minCostToMoveChips(position)
assert(ans == res)

position = [2,2,3,3,3]
ans = 2
res = su.minCostToMoveChips(position)
assert(ans == res)

position = [1]
ans = 0
res = su.minCostToMoveChips(position)
assert(ans == res)

position = [1,1,1,1]
ans = 0
res = su.minCostToMoveChips(position)
assert(ans == res)

position = [1,1,1,1,2,2,3,3,3]
ans = 2
res = su.minCostToMoveChips(position)
assert(ans == res)

position = [6,4,7,8,2,10,2,7,9,7]
ans = 4
res = su.minCostToMoveChips(position)
assert(ans == res)
