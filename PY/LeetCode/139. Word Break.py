from typing import List
from functools import lru_cache
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        string = s
        for _ in range(len(s)):
            for word in wordDict:
                if string.startswith(word):
                    string = string[len(word):]
                    break
        print(string)
        return True if not string else False

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        @lru_cache(None)
        def dfs(string):
            if not string: return True
            for word in wordDict:
                if string.startswith(word):
                    if dfs(string[len(word):]):
                        return True
            return False
                    
        return dfs(s)

su = Solution()

# case bug
s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
wordDict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
res = su.wordBreak(s, wordDict)
ans = False
assert(res == ans)

# case std1
s = "leetcode"
wordDict = ["leet","code"]
res = su.wordBreak(s, wordDict)
ans = True
assert(res == ans)

# case std2

# case std3
s = "catsandog"
wordDict = ["cats","dog","sand","and","cat"]
res = su.wordBreak(s, wordDict)
ans = False
assert(res == ans)
