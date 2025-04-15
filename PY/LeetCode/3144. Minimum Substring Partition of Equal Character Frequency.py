import collections
class Solution:
    def minimumSubstringsInPartition0(self, s: str) -> int:
        l = len(s)
        dp = [0]+[l]*l
    
        for i in range(l):
            count = collections.defaultdict(int)
            print(s[i], i, dp)
            for j in range(i,l):
                count[s[j]] += 1
                if len(set(count.values())) == 1:
                    dp[j+1] = min(dp[j+1],dp[i]+1) 
                print("-|", j, dp)
        # 为什么dp[-1]是最小的？因为执行if == 1后，必然是合并了一些字符，所以肯定比最大值len(s)小
        # 为什么dp定义为任意开头i，到指定j结尾的子串，而dp[-1]能够代表[i, j]最小的字串，而不是[i, j]内某一个？以为若不是从i开始，而是中间开始的子串，计算是还要额外加上1
        return dp[-1]
    

    def minimumSubstringsInPartition(self, s: str) -> int:
        dp = [0] + [float("inf")] * len(s)

        for i in range(len(s)):
            d = {}
            for j in range(i, len(s)):
                d[s[j]] = d.get(s[j], 0) + 1
                if len(set(d.values())) == 1:
                    dp[j+1] = min(dp[i]+1, dp[j+1])
        return dp[-1]

su = Solution()
s = "fabccddg"
ans = 3
res = su.minimumSubstringsInPartition(s)
assert(res == ans)


s = "cab"
ans = 1
res = su.minimumSubstringsInPartition(s)
assert(res == ans)