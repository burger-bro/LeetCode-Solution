from typing import List
from collections import defaultdict

class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        len2words = defaultdict(list)
        for idx, word in enumerate(words):
            len2words[len(word)].append(idx)
        
        def hamming(word1, word2):
            dff = 0
            for i in range(len(word1)):
                if word1[i] != word2[i]:
                    dff += 1
            return dff == 1

        ans = []
        def helper(words_idx):
            nonlocal ans
            tmp = [words[words_idx[0]]]
            last = words_idx[0]
            for i in words_idx[1:]:
                print(i, groups[i] == groups[last], words[i], words[last], hamming(words[i], words[last]))
                if groups[i] != groups[last] and hamming(words[i], words[last]):
                    tmp.append(words[i])
                    last = i
            print(tmp)
            if len(tmp) > len(ans):
                ans = tmp

        for ww in len2words.values():
            helper(ww)
        
        return ans

    # def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
    #     len2words = defaultdict(list)
    #     for idx, word in enumerate(words):
    #         len2words[len(word)].append(idx)
        
    #     def hamming(word1, word2):
    #         dff = 0
    #         for i in range(len(word1)):
    #             if word1[i] != word2[i]:
    #                 dff += 1
    #         return dff == 1

    #     ans = []
    #     def helper(words_idx):
    #         nonlocal ans
    #         for i in range(len(words_idx)):
    #             tmp = [words[words_idx[i]]]
    #             last = i
    #             for j in range(i+1, len(words_idx)):
    #                 if groups[words_idx[j]] != groups[words_idx[last]] and \
    #                     hamming(words[words_idx[j]], words[words_idx[last]]):
    #                     tmp.append(words[words_idx[j]])
    #                     last = j
    #             if len(tmp) > len(ans):
    #                 ans = tmp

    #     for ww in len2words.values():
    #         helper(ww)
    #     print(ans)
    #     return ans


su = Solution()
# case std1
words = ["bab","dab","cab"]
groups = [1,2,2]
res = su.getWordsInLongestSubsequence(words, groups)

# case std2
words = ["bad","dc","bc","ccd","dd","da","cad","dba","aba"]
groups = [9,7,1,2,6,8,3,7,2]
res = su.getWordsInLongestSubsequence(words, groups)
