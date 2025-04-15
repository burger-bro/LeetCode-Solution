from typing import List

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        char2last_idx = dict()
        for i, c in enumerate(s):
            char2last_idx[c] = i
        cur_end = size = 0
        ret = []
        for i, c in enumerate(s):
            size += 1
            cur_end = max(char2last_idx[c], cur_end)
            if i == cur_end:
                ret.append(size)
                size = 0
        print(ret)
        return ret
    
    # def partitionLabels(self, s: str) -> List[int]:
    #     last_char = dict()
    #     for i, c in enumerate(s):
    #         last_char[c] = i
    #     print(last_char)
    #     cur_set = set()
    #     ret = []
    #     last_idx = 0
    #     for i, c in enumerate(s):
    #         cur_set.add(c)
    #         flag = True
    #         for cc in cur_set:
    #             if last_char[cc] > i:
    #                 flag = False
    #                 break
    #         if flag:
    #             ret.append(i-last_idx+1)
    #             cur_set.clear()
    #             last_idx = i+1
    #     print(ret)
    #     return ret

su = Solution()
# case std1
s = "ababcbacadefegdehijhklij"
res = su.partitionLabels(s)
ans = [9, 7, 8]
assert(res == ans)
# case std2
s = "eccbbbbdec"
res = su.partitionLabels(s)
ans = [10]
assert(res == ans)
# case std3
s = "abcdefghijklmn"
res = su.partitionLabels(s)
ans = [1,1,1,1,1,1,1,1,1,1,1,1,1,1]
assert(res == ans)
