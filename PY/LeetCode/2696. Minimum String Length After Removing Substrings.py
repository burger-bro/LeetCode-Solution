class Solution:
    def minLength0(self, s: str) -> int:
        if len(s) == 1: return 1
        p1, p2 = 0, 1
        cnt = 0
        existed = [True] * len(s)
        print("start")
        while p2 < len(s):
            if (s[p1] == "A" and s[p2] == "B") or (s[p1] == "C" and s[p2] == "D"):
                print(p1, p2)
                existed[p1], existed[p2] = False, False
                # if p1 != 0:
                #     p1 = p1 - 1
                #     p2 = p2 + 1
                # else:
                #     p1 = p2 + 1
                #     p2 = p1 + 1
                tmp = p1 - 1
                while tmp >= 0 and not existed[tmp]:
                    tmp -= 1
                if tmp == -1:
                    p1 = p2 + 1
                    p2 = p1 + 1
                else:
                    p1 = p1 - 1
                    p2 = p2 + 1
                # print(p1, p2)
                cnt += 2
            else:
                p1 += 1
                p2 += 1
        print(len(s) - cnt)
        return len(s) - cnt
    
    def minLength1(self, s: str) -> int:
        if len(s) == 1: return 1
        tmp = s
        while True:
            for i in range(0, len(tmp)-1):
                if (tmp[i] == "A" and tmp[i+1] == "B") or (tmp[i] == "C" and tmp[i+1] == "D"):
                    tmp = tmp[:i] + tmp[i+2:]
                    break
            else:
                break
        # print(len(tmp))
        return len(tmp)

    def minLength(self, s: str) -> int:
        if len(s) == 1: return 1
        stack = []
        for c in s:
            if not stack:
                stack.append(c)
            elif stack[-1] == "C" and c == "D":
                stack.pop()
            elif stack[-1] == "A" and c == "B":
                stack.pop()
            else:
                stack.append(c)

        return len(stack)


su = Solution()
s = "ABFCACDB"
ans = 2
res = su.minLength(s)
assert(res == ans)

s = "ACBBD"
ans = 5
res = su.minLength(s)
assert(res == ans)

s = "ABABAB"
ans = 0
res = su.minLength(s)
assert(res == ans)

s = "CDCDCD"
ans = 0
res = su.minLength(s)
assert(res == ans)

s = "CDABCD"
ans = 0
res = su.minLength(s)
assert(res == ans)

s = "CCABDD"
ans = 0
res = su.minLength(s)
assert(res == ans)

s = "CCADDAB"
ans = 5
res = su.minLength(s)
assert(res == ans)

s = "CCDAABBDCD"
ans = 0
res = su.minLength(s)
assert(res == ans)

