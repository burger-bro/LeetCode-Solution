def _print(*str):
    flag = False
    if flag:
        print(str)

class Solution:
    def simplifyPath(self, path: str) -> str:
        path_list = []
        # split ///
        start = -1
        i = 0
        end_flag = False
        while i < len(path):
            if start == -1:
                while path[i] == '/':
                    _print(i, len(path), path[i])
                    i += 1
                    if i > len(path) - 1:
                        break
                # if end_flag: break
                start = i
            i += 1
            if start != -1 and i < len(path):
                
                while path[i] != '/':
                    i += 1
                    if i == len(path):
                        end_flag = True
                        break
                end = i
            else:
                end = len(path)
            print(start, end)
            _print(path[start:end])
            tmp_path = path[start:end]
            if tmp_path == '..':
                if path_list:
                    path_list.pop()
            elif not tmp_path or tmp_path == '.':
                pass
            else:
                path_list.append(tmp_path)
            start = -1

            if end_flag:
                break
        _print(path_list)
        ret = '/'+'/'.join(path_list)
        _print(ret)
        return ret

su = Solution()

# case14
path = "//////home/user/Documents/../Pictures/s"
ans = "/home/user/Pictures/s"
res = su.simplifyPath(path)
assert(res == ans)
# exit()

# case1
path = "/home/"
ans = "/home"
res = su.simplifyPath(path)
assert(res == ans)
# case2
path = path = "/home//foo/"
ans = "/home/foo"
res = su.simplifyPath(path)
assert(res == ans)
# case3
path = "/home/user/Documents/../Pictures"
ans = "/home/user/Pictures"
res = su.simplifyPath(path)
assert(res == ans)
# case4
path = "/../"
ans = "/"
res = su.simplifyPath(path)
assert(res == ans)
# case5
path = "/.../a/../b/c/../d/./"
ans = "/.../b/d"
res = su.simplifyPath(path)
assert(res == ans)
# case6
path = "//////home/user/Documents/../Pictures"
ans = "/home/user/Pictures"
res = su.simplifyPath(path)
assert(res == ans)
# case7
path = "//////home///////user//////Documents/////..//////Pictures//////"
ans = "/home/user/Pictures"
res = su.simplifyPath(path)
assert(res == ans)
# case8
path = "//////home///////user//.......////Documents/////..//////Pictures//////"
ans = "/home/user/......./Pictures"
res = su.simplifyPath(path)
assert(res == ans)
# case9
path = "/home/user/Documents/../Pictures/...../.../...../"
ans = "/home/user/Pictures/...../.../....."
res = su.simplifyPath(path)
assert(res == ans)
# case10
path = "/home/user/Documents/../Pictures/...../.../...../.."
ans = "/home/user/Pictures/...../..."
res = su.simplifyPath(path)
assert(res == ans)
# case11
path = "/home/user/Documents/../Pictures/...../.../...../../../../../../../"
ans = "/"
res = su.simplifyPath(path)
assert(res == ans)
# case12
path = "/././././/home/user/Documents/../Pictures/././././././././././././"
ans = "/home/user/Pictures"
res = su.simplifyPath(path)
assert(res == ans)
# case13
path = "/././././/home/..user../Documents/../Pictures/././././././././././././"
ans = "/home/..user../Pictures"
res = su.simplifyPath(path)
assert(res == ans)
# case14
print("test")
path = "/home/..user../Documents/../Pictures/"
ans = "/home/..user../Pictures"
res = su.simplifyPath(path)
assert(res == ans)
