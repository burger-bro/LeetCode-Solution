from typing import List

class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        all_graph = []
        idx2set = {}

        # nums = [2,5,6,8]
        # maxDiff = 2

        tmp_set = set()
        last = nums[0]
        for i, num in enumerate(nums):
            if abs(num-last) > maxDiff:
                all_graph.append(tmp_set)
                tmp_set = set([i])
            else:
                tmp_set.add(i)
            last = num
        all_graph.append(tmp_set)

        for i, g in enumerate(all_graph):
            for idx in g:
                idx2set[idx] = all_graph[i]
            

        ret = []
        for q in queries:
            exist = idx2set[q[0]] is idx2set[q[1]]
            ret.append(exist)

        print(ret)

        return ret

    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        all_graph = []
        idx2graph = {}

        tmp_graph = set()
        last = nums[0]
        for i, num in enumerate(nums):
            if abs(num-last) > maxDiff:
                all_graph.append(tmp_graph)
                tmp_graph = set([i])
            else:
                tmp_graph.add(i)
            last = num
        all_graph.append(tmp_graph)

        for i, g in enumerate(all_graph):
            for idx in g:
                idx2graph[idx] = all_graph[i]
            
        ret = []
        for q in queries:
            exist = idx2graph[q[0]] is idx2graph[q[1]]
            ret.append(exist)

        print(ret)

        return ret


su = Solution()
# case std1
n = 2
nums = [1,3]
maxDiff = 1
queries = [[0,0],[0,1]]
res = su.pathExistenceQueries(n, nums, maxDiff, queries)
ans = [True, False]
assert(res == ans)
# case std2
n = 4
nums = [2,5,6,8]
maxDiff = 2
queries = [[0,1],[0,2],[1,3],[2,3]]
res = su.pathExistenceQueries(n, nums, maxDiff, queries)
ans = [False,False,True,True]
assert(res == ans)


