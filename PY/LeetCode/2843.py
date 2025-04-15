class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        cnt = 0
        for i in range(low, high+1):
            str_i = str(i)
            if len(str_i) % 2 != 0:
                continue
            x = sum(map(lambda x: int(x), list(str_i[:len(str_i)//2])))
            y = sum(map(lambda x: int(x), list(str_i[len(str_i)//2:])))
            if x == y:
                cnt += 1    
        return cnt

    def countSymmetricIntegers(self, low: int, high: int) -> int:
        cnt = 0
        for n in range(low, high+1):
            if 10 <= n <= 99:
                if n%10 == n//10:
                    cnt += 1
            elif 1000 <= n <= 9999:
                if (n//100)%10 + n//1000 == (n%100)//10 + n%10:
                    cnt += 1
        return cnt



su = Solution()
# cast std1
low, high = 1, 100
res = su.countSymmetricIntegers(low, high)
ans = 9
assert(res == ans)

# cast std2
low, high = 1200, 1230
res = su.countSymmetricIntegers(low, high)
ans = 4
assert(res == ans)

