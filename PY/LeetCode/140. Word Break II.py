from typing import List
from functools import lru_cache

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        @lru_cache(None)
        def dfs(string):
            if not string: return [[]]
            cur_ans = []
            for word in wordDict:
                if string.startswith(word):
                    ret = dfs(string[len(word):])
                    for r in ret:
                        tmp = [word]
                        tmp.extend(r)
                        cur_ans.append(tmp)
            return cur_ans
                    
        return [" ".join(words) for words in dfs(s)]

su = Solution()
# case std1
s = "catsanddog"
wordDict = ["cat","cats","and","sand","dog"]
ans = ["cats and dog","cat sand dog"]
res = su.wordBreak(s, wordDict)
print(res)
assert(res == ans)

