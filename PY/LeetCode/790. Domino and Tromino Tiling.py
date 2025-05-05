class Solution:
    def numTilings(self, n: int) -> int:
        ans = [0] * n
        ans[0] = 1
        ans[1] = 2
        ans[2] = 5
        for i in range(3, n):
            ans[i] = 2*ans[i-1] + ans[i-3]
        return ans[n-1]

su = Solution()
print(su.numTilings(3))
print(su.numTilings(4))
print(su.numTilings(5))
