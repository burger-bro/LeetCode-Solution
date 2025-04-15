from typing import List
from collections import Counter, deque


class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        last_idx = [-1] * len(word2)
        idx_cnt = len(word2) - 1
        for i in range(len(word1)-1, -1, -1):
            if word2[idx_cnt] == word1[i]:
                last_idx[idx_cnt] = i
                idx_cnt -= 1
        print(last_idx)

        ans = []
        cnt = 0
        taken = False
        for i in range(len(word1)):
            if cnt >= len(word2):
                return ans
            if word1[i] == word2[cnt]:
                ans.append(i)
                cnt += 1
            else:
                if taken:
                    continue
                if last_idx[cnt] < i:
                    ans.append(i)
                    taken = True
                    cnt += 1
        return []
        


su = Solution()

word1 = "vbcca"
word2 = "abc"
res = su.validSequence(word1, word2)
ans = [0, 1, 2]
assert(res == ans)

word1 = "abbabc"
word2 = "abc"
