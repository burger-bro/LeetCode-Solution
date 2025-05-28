from typing import List

class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        ret = []
        for idx, word in enumerate(words):
            if x in word:
                ret.append(idx)
        return ret
        


su = Solution()

