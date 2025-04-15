class Solution:
    def kthCharacter(self, k: int) -> str:
        start = 'a'
        # print(ord(start), chr(97))
        j = 0
        cnt = 1
        sum = 1
        while sum < k:
            j += 1
            sum += cnt
            cnt *= 2
        cnt = cnt // 2
        tmp = k - (sum - cnt) - 1
        i = 0
        print("cnt", cnt)
        while cnt:
            cnt = cnt // 2
            if tmp < cnt:
                i += 1
        print(tmp, j, i)
        tmp = max(tmp + j - i, 0)
        # print(sum, cnt, tmp)
        return chr(ord(start) + tmp)
    
"abbcbccd"

    # def kthCharacter(self, k: int) -> str:
    #     start = 'a'
    #     cnt = 1
    #     sum = 1
    #     while len(start) < k:
    #         cnt *= 2
    #         sum += cnt
    #         tmp_str = ""
    #         for ch in start:
    #             tmp_str += chr(ord(ch) + 1)
    #         start += tmp_str
    #     # print(start)

    #     #debug
    #     tmp_num_str = ''
    #     for ch in start:
    #         tmp_num_str += str(ord(ch)-97)
    #     # print(tmp_num_str)
    #     #

    #     return start[k-1]

su = Solution()
print(su.kthCharacter(5))
print(su.kthCharacter(10))
print(su.kthCharacter(33))
print(su.kthCharacter(37))
print(su.kthCharacter(59))
print(su.kthCharacter(83))