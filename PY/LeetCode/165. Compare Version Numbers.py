class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        # version1, version2 = 0, 0
        v1 = version1.split('.')
        v2 = version2.split('.')
        v1 = [int(v) for v in v1]
        v2 = [int(v) for v in v2]
        redundant = abs(len(v1) - len(v2))
        shorter = v1 if len(v1) < len(v2) else v2
        for _ in range(redundant):
            shorter.append(0)
            
        print(v1, v2)
        if v1 > v2:
            return 1
        elif v1 < v2:
            return -1
        else:
            return 0

su = Solution()


# case std1
version1 = "1.2"
version2 = "1.10"
ans = -1
res = su.compareVersion(version1, version2)
assert(res == ans)


# case std2
version1 = "1.01"
version2 = "1.001"
ans = 0
res = su.compareVersion(version1, version2)
assert(res == ans)


# case std3
version1 = "1.0"
version2 = "1.0.0.0"
ans = 0
res = su.compareVersion(version1, version2)
assert(res == ans)
exit(0)

