class Solution:
    def trailingZeroes(self, n: int) -> int:
        n = 9492
        limit = pow(10, 10)
        t = 1
        zero_num = 0
        tail = 1
        for i in range(1, n+1):
            t *= i
            tail = (tail * i) % limit
            while tail % 10 == 0:
                zero_num += 1
                tail = tail//10
            # print(t)
        print(zero_num)
        return zero_num

    def trailingZeroes(self, n: int) -> int:
        five, two = 0, 0
        for i in range(1, n+1):
            while i > 2 or i > 5:
                if i % 5 == 0:
                    five += 1
                    i = i // 5
                elif i % 2 == 0:
                    two += 1
                    i = i // 2
                else:
                    break
        print(five, two)
        return min(five, two)

su = Solution()
# case debug
n = 6
ans = 1
res = su.trailingZeroes(n)
assert(res == ans)


# case std1
n = 3
ans = 0
res = su.trailingZeroes(n)
assert(res == ans)

# case std2
n = 5
ans = 1
res = su.trailingZeroes(n)
assert(res == ans)
# case std3
n = 0
ans = 0
res = su.trailingZeroes(n)
assert(res == ans)
