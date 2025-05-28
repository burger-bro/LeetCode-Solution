class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        num1, num2 = 0, 0
        for i in range(1, n+1):
            if i % m == 0:
                num2 += i
            else:
                num1 += i
        return num1-num2
    
    def differenceOfSums(self, n: int, m: int) -> int:
        all_sum = sum(i for i in range(1, n+1))
        num2 = 0
        k = m
        while k <= n:
            num2 += k
            k += m
        return all_sum-2*num2