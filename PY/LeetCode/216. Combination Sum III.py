from typing import List

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        used_num = [False for _ in range(9)]
        ans_set = []
        def dfs(_n, _cnt, _used_num, index):
            if _cnt == k and _n == 0:
                ans_set.append([i+1 for i in range(len(used_num)) if used_num[i]])
                return

            if _cnt > k or _n == 0:
                return
            
            for i in range(index, 0, -1):
                if i > _n or used_num[i-1]:
                    continue
                _used_num[i-1] = True
                dfs(_n-i, _cnt+1, _used_num, i-1)
                _used_num[i-1] = False
        dfs(n, 0, used_num, 9)
        return ans_set

    # def combinationSum3(self, k: int, n: int) -> List[List[int]]:
    #     ans_set = []
    #     def dfs(ans, cnt):
    #         if len(ans) == k:
    #             if sum(ans) == n:
    #                 ans_set.append(ans)
    #             return
            
    #         for i in range(cnt, 10):
    #             if sum(ans)+i<=n:
    #                 dfs(ans+[i], i+1)
                    
    #     dfs([], 1)
    #     print(ans_set)
    #     return ans_set

    # def combinationSum3(self, k: int, n: int) -> List[List[int]]:
    #     ret = []
    #     def dfs(index,prev,total):
    #         if len(prev) ==k:
    #             if total==n:
    #                 ret.append(prev)
    #             return
            
    #         for i in range(index,10):           
    #                 curr=total+i
    #                 if curr<=n:
    #                     dfs(i+1,prev+[i],curr)
    #     dfs(1,[],0)
    #     print(ret)
    #     return ret

su = Solution()
# k = 3
# n = 7
# su.combinationSum3(k, n)
# print([i for i in range(9, 0, -1)])

k = 3
n = 9
su.combinationSum3(k, n)

k = 2
n = 15
su.combinationSum3(k, n)

# k = 4
# n = 1
# su.combinationSum3(k, n)








