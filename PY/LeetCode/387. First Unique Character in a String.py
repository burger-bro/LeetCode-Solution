class Solution:
    def firstUniqChar(self, s: str) -> int:
        letter_indtx_dict = {}
        for i in range(len(s)):
            if s[i] in letter_indtx_dict:
                letter_indtx_dict[s[i]] = -1
            else:
                letter_indtx_dict[s[i]] = i
        res = float("inf")
        for id in letter_indtx_dict.values():
            if id == -1:
                continue
            res = min(res, id)
        return res if res != float("inf") else -1
        