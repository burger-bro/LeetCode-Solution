from typing import List

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen, ret = set(), set()
        for i in range(10, len(s)+1):
            t = s[i-10:i]
            if t in seen:
                ret.add(t)
            seen.add(t)
        return list(ret)


        