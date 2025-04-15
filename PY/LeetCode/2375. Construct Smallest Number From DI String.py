class Solution:
    def smallestNumber(self, pattern: str) -> str:
        ret = "9" * (len(pattern)+1)
        num_dict = {str(i): True for i in range(1, 10)}
        def dfs(num_dict, i, cur):
            nonlocal ret
            if len(cur) == len(pattern)+1:
                ret = min(ret, cur)
                return
            op = (lambda x,y: x>y) if pattern[i] == 'I' else (lambda x,y: x<y)
                        
            for k, v in num_dict.items():
                if not v:
                    continue
                if cur and op(cur[-1], k):
                    continue
                num_dict[k] = False
                dfs(num_dict, i+1, cur+k)
                num_dict[k] = True
        dfs(num_dict, -1, "")
        return ret

    def smallestNumber(self, pattern: str) -> str:
        pattern += 'I' # 最巧妙的一句，对于那些在最后一位要做特殊处理的算法，思考在原始迭代上多增加一个dummy可能会将逻辑大大简化
        stack = []
        ret = ""
        cnt = 0
        cur_num = 1
        while cnt < len(pattern):
            print(stack, ret)
            stack.append(cur_num)
            if pattern[cnt] == "I":
                while stack:
                    ret += str(stack.pop())
            cur_num += 1
            cnt += 1
        print(ret)
        return ret

# op = lambda x,y: x>y if 'I' else lambda x,y: x<y

# print(op)
# print(op(2,3))

# exit(0)
su = Solution()

# case1
pattern = "I"
res = su.smallestNumber(pattern)
ans = "12"
assert(res == ans)

# case2
pattern = "D"
res = su.smallestNumber(pattern)
ans = "21"
assert(res == ans)

# case3
pattern = "IIIIIIII"
res = su.smallestNumber(pattern)
ans = "123456789"
assert(res == ans)

# case std1
pattern = "IIIDIDDD" #  I I I D I D D D
                     # 1 2 3 5 4 9 8 7 6
res = su.smallestNumber(pattern)
ans = "123549876"
assert(res == ans)

# case std2
pattern = "DDD"
res = su.smallestNumber(pattern)
ans = "4321"
assert(res == ans)
