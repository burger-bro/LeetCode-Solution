class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        """
        问题抽象为 在len(finish)-len(s)的范围内 有多少的前缀能使得
        """
        prefix_len = len(str(finish)) - len(s)
        s_start = str(start)
        s_finish = str(finish)
        start_prefix = s_start[:prefix_len] if prefix_len<=len(s_start) else "0"
        finish_prefix = s_finish[:prefix_len]
        # start_prefix += str(start_prefix)[-len(s)-1:] ...
        start_prefix = (len(finish_prefix)-len(start_prefix)) * '0' + start_prefix
        print(start_prefix, finish_prefix)
        # 找到start_prefix到finish_prefix之间有多少每一位小于limit的数
        # 注意处理边界条件
        # 6000 -> 124
        # 1 2000 655321 -> 321
        # 1(1321) - 655 
        # limit=5    001-200    0-1 0-5 0-5

        def calc_number(start_, finish_):
            print("start")
            cnt = max((int(finish_[0]) - int(start_[0])), 1)
            for idx in range(1, len(start_)):
                cnt *= limit - int(start_[idx]) + 1
                print(cnt)

        calc_number(start_prefix, finish_prefix)
        calc_number(start_prefix[1:], finish_prefix[1:])
        calc_number(start_prefix[2:], finish_prefix[2:])


su = Solution()

# case 1 6223 124

# case1
start = 1
finish = 2001
limit = 5
s = "1"
res = su.numberOfPowerfulInt(start, finish, limit, s)
ans = 73
assert(res == ans)


# case std1
start = 1
finish = 6000
limit = 4
s = "124"
res = su.numberOfPowerfulInt(start, finish, limit, s)
ans = 5
assert(res == ans)



