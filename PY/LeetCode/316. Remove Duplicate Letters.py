from collections import Counter

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        letter_dict = Counter(s) #{ch: 0 for ch in "abcdefghijklmnopqrstuvwxyz"}

        result = []
        visited = set()

        for ch in s:
            letter_dict[ch] -= 1
            if ch in visited:
                continue
            while result and ch < result[-1] and letter_dict[result[-1]] > 0:
                visited.remove(result.pop())
            result.append(ch)
            visited.add(ch)
                
        print(result)
        return "".join(result)

su = Solution()

case1 = "bcabc"
res = su.removeDuplicateLetters(case1)
assert res == "abc"

case2 = "cbacdcbc"
res = su.removeDuplicateLetters(case2)
assert res == "acdb"

case3 = "cdadabcc"
res = su.removeDuplicateLetters(case3)
assert res == "adbc"

case4 = "bbcaac"
res = su.removeDuplicateLetters(case4)
assert res == "bac"

case5 = "abacb"
res = su.removeDuplicateLetters(case5)
assert res == "abc"
