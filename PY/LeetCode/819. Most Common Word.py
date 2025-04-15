from typing import List
import re
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = re.split(r"([\!|\.|\?|\'|\,|\;| ])", paragraph)
        print(paragraph)
        banned.extend(['', ' ', '.', '!', '?', ';', "\'"])
        banned = list(map(lambda x:x.lower(), banned))
        d = {}
        max_cnt = 0
        most_com = None
        for p in paragraph:
            p = p.lower()
            if p in banned:
                continue
            d[p] = d.get(p, 0) + 1
            if d[p] > max_cnt:
                max_cnt = d[p]
                most_com = p
        print(most_com, d)
        return most_com

    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = re.split(r"\W+", paragraph.lower())
    
        banned = set(map(lambda x:x.lower(), banned))
        d = {}
        max_cnt = 0
        most_com = None
        for p in paragraph:
            if p in banned:
                continue
            d[p] = d.get(p, 0) + 1
            if d[p] > max_cnt:
                max_cnt = d[p]
                most_com = p
        print(most_com, d)
        return most_com

su = Solution()
paragraph = "Bob. hIt, baLl" # "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["bob", "hit"]
res = su.mostCommonWord(paragraph, banned)