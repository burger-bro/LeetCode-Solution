from typing import List
from collections import deque
import heapq as hq

class Solution:
    def unmarkedSumArray(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        ret = []
        # nums_dict = {}
        # for i in range(len(nums)):
        #     if nums[i] not in nums_dict:
        #         nums_dict[nums[i]] = set([i])
        #     else:
        #         nums_dict[nums[i]].add(i)
        # print(nums_dict)

        nums_dict = {i: nums[i] for i in range(len(nums))}
        # 错误排序稳定性
        # idx_array = sorted([i for i in range(len(nums)-1)], key=lambda x:nums_dict[x], reverse=True)
        # 正确1
        idx_array = sorted([i for i in range(len(nums)-1, -1, -1)], key=lambda x:nums_dict[x], reverse=True)
        # 正确2
        # idx_array = sorted([i for i in range(len(nums))], key=lambda x:nums_dict[x])
        # idx_array = idx_array[::-1]

        # idx_array = deque(sorted([i for i in range(len(nums))], key=lambda x:nums_dict[x]))
        # print(idx_array)
        marked = [False] * len(nums)
        sums = sum(nums)
        print("begin")
        for q in queries:
            # debug
            tmp_list = []
            for i in range(len(marked)):
                if not marked[i]:
                    tmp_list.append(str(nums[i]))
                else:
                    tmp_list.append('#'*len(str(nums[i])))
                
            print("marked:", f"[{','.join(tmp_list)}]")
            # debug

            if not marked[q[0]]:
                marked[q[0]] = True
                sums -= nums[q[0]]
                # num_array.pop(q[0])
                # del_idx = -1
                # for i in range(len(num_array)):
                #     if num_array[i] == q[0]:
                #         del_idx = i
                #         break
                idx_array.remove(q[0])
            # print("sums1", sums)
            cnt = q[1]
            while cnt and idx_array:
                cnt -= 1
                mark_idx = idx_array.pop()
                # mark_idx = num_array.popleft()
                marked[mark_idx] = True
                sums -= nums[mark_idx]
            print("sums2", sums)
            ret.append(sums)
        print(ret)
        return ret
        
    def unmarkedSumArray(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        ret = []

        num_idx = [(n, i) for i, n in enumerate(nums)]
        hq.heapify(num_idx)
        
        marked = set()
        sums = sum(nums)
        for q in queries:
            if q[0] not in marked:
                sums -= nums[q[0]]
                marked.add(q[0])
            cnt = q[1]
            while cnt and num_idx:
                _, idx = hq.heappop(num_idx)
                if idx not in marked:
                    sums -= nums[idx]
                    marked.add(idx)
                    cnt -= 1
            ret.append(sums)
        # print(ret)
        return ret


su = Solution()
nums = [1,2,2,1,2,3,1]
queries = [[1,2],[3,3],[4,2]]
ans = [8, 3, 0]
res = su.unmarkedSumArray(nums, queries)
assert(res == ans)


nums =  [1,4,2,3]
queries = [[0,1]]
ans = [7]
res = su.unmarkedSumArray(nums, queries)
assert(res == ans)


nums =  [1,2,3,4,5,6,7,8,9]
queries = [[0,10], [1,2]]
ans = [0, 0]
res = su.unmarkedSumArray(nums, queries)
assert(res == ans)

nums =  [1,2,3,4,5,6,7,8,9]
queries = [[0,7]]
ans = [9]
res = su.unmarkedSumArray(nums, queries)
assert(res == ans)

nums =  [1,2,3]
queries = [[0,0]]
ans = [5]
res = su.unmarkedSumArray(nums, queries)
assert(res == ans)

nums =  [1,2,3]
queries = [[2,0]]
ans = [3]
res = su.unmarkedSumArray(nums, queries)
assert(res == ans)

nums =  [1,2,3]
queries = [[1,0]]
ans = [4]
res = su.unmarkedSumArray(nums, queries)
assert(res == ans)

nums =  [1,2,2,3,4,2,2,3]
queries = [[7,3], [3, 0]]
ans = [11, 8]
res = su.unmarkedSumArray(nums, queries)
# print(res)
assert(res == ans)

nums =  [1,2,2]
queries = [[1, 999]]
ans = [0]
res = su.unmarkedSumArray(nums, queries)
# print(res)
assert(res == ans)

nums =  [18,5,5,5,5,18,13,5,10,13,18,13,19,14,14,13,14,13,11]
"""
0[18,5,5,5,5,18,13,5,10,13,18,13,19,14,14,13,14,13,11] #226
1[18,5,5,5,5,18,##,5,10,13,18,13,19,14,14,13,14,13,11] #213
2[18,#,5,5,5,18,##,5,10,13,18,13,19,14,##,13,14,13,11] #194
3[18,#,#,#,#,18,##,5,10,13,18,13,19,##,##,13,14,13,11] #165
4[18,#,#,#,#,18,##,#,##,13,18,13,19,##,##,13,14,13,##] #139
"""
[18,18,5,10,13,18,13,19,13,14,13,11]
queries = [[6,0],[14,1],[13,3],[7,2],[5,2],[8,1],[5,3],[9,0],[4,2],[4,4],[9,2],[15,0],[1,3],[13,1],[11,0],[16,4],[3,2],[17,3],[11,1]]
ans = [213, 194, 165, 139, 95, 82, 37, 37, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
res = su.unmarkedSumArray(nums, queries)
# print(res)
assert(res == ans)

