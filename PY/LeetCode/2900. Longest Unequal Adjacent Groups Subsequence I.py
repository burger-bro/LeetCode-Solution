from typing import List

class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        cur = -1
        sub_idx = []
        for idx, g in enumerate(groups):
            if g != cur:
                cur = g
                sub_idx.append(idx)
        return [words[idx] for idx in sub_idx]


