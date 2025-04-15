class Solution:
    def isNumber(self, s: str) -> bool:
        print(f"********************start{s}********************")
        def is_digits(num: str) -> bool:
            for n in num:
                if not n.isdigit():
                    return False
            return True

        # deal with sign
        print("sign")
        if s[0] == '+' or s[0] == '-':
            s = s[1:]
        if s and (s[0] == '+' or s[0] == '-'):
            return False
        # split exponent
        valid = set(str(i) for i in range(10)) | {'+', '-', '.', 'e', 'E'}
        exp_idx = -1
        # split base and exp
        for i, c in enumerate(s):
            if c not in valid:
                return False
            if c == 'e' or c == 'E':
                if exp_idx != -1: return False
                exp_idx = i
        if exp_idx != -1:
            exp = s[exp_idx+1:]
            base = s[:exp_idx]
        else:
            exp = ''
            base = s
        # deal with empty base
        print("empty base")
        if not base: return False
        # split dot
        print("dot")
        if base.count('.') > 1: return False
        dot_idx = base.index('.') if '.' in base else -1
        if dot_idx != -1:
            num1 = base[:dot_idx]
            num2 = base[dot_idx+1:]
        else:
            num1 = base
            num2 = ''
        print(f"num1:{num1}, num2:{num2}, exp:{exp}")
        # deal with empty base
        if exp_idx != -1 and ((not num1 and not num2) or not exp):
            return False
        if not num1 and not num2 and not exp: return False
        return is_digits(num1) and is_digits(num2) and is_digits(exp)


    def isNumber(self, s: str) -> bool:
        print(f"********************start{s}********************")
        def is_digits(num: str) -> bool:
            for n in num:
                if not n.isdigit():
                    return False
            return True

        def strip_sign(s):
            # deal with sign
            print("sign")
            if not s: return True, s
            ret_flag = True
            if s[0] == '+' or s[0] == '-':
                s = s[1:]
            if s and (s[0] == '+' or s[0] == '-'):
                ret_flag = False
            return ret_flag, s

        # split exponent
        valid = set(str(i) for i in range(10)) | {'+', '-', '.', 'e', 'E'}
        exp_idx = -1
        # split base and exp
        for i, c in enumerate(s):
            if c not in valid:
                return False
            if c == 'e' or c == 'E':
                if exp_idx != -1: return False
                exp_idx = i
        if exp_idx != -1:
            exp = s[exp_idx+1:]
            base = s[:exp_idx]
        else:
            exp = ''
            base = s
        flag, base = strip_sign(base)
        if not flag: return False
        flag, exp = strip_sign(exp)
        if not flag: return False
        # deal with empty base
        print("empty base")
        if not base: return False
        # split dot
        print("dot")
        if base.count('.') > 1: return False
        dot_idx = base.index('.') if '.' in base else -1
        if dot_idx != -1:
            num1 = base[:dot_idx]
            num2 = base[dot_idx+1:]
        else:
            num1 = base
            num2 = ''
        flag, num1 = strip_sign(num1)
        if not flag: return False
        print(f"num1:{num1}, num2:{num2}, exp:{exp}")
        # deal with empty base
        if exp_idx != -1 and ((not num1 and not num2) or not exp):
            return False
        if not num1 and not num2 and not exp: return False
        return is_digits(num1) and is_digits(num2) and is_digits(exp)


    def isNumber(self, s: str) -> bool:
        print(f"********************start{s}********************")
        def is_digits(num: str) -> bool:
            for n in num:
                if not n.isdigit():
                    return False
            return True

        def strip_sign(s):
            # deal with sign
            print("sign")
            if not s: return True, s
            ret_flag = True
            if s[0] == '+' or s[0] == '-':
                s = s[1:]
            if s and (s[0] == '+' or s[0] == '-'):
                ret_flag = False
            return ret_flag, s

        # split exponent
        valid = set(str(i) for i in range(10)) | {'+', '-', '.', 'e', 'E'}
        exp_idx = -1
        # split base and exp
        for i, c in enumerate(s):
            if c not in valid:
                return False
            if c == 'e' or c == 'E':
                if exp_idx != -1: return False
                exp_idx = i
        if exp_idx != -1:
            exp = s[exp_idx+1:]
            base = s[:exp_idx]
        else:
            exp = ''
            base = s
        flag, base = strip_sign(base)
        if not flag: return False
        flag, exp = strip_sign(exp)
        if not flag: return False
        # deal with empty base
        print("empty base")
        if not base: return False
        # split dot
        print("dot")
        if base.count('.') > 1: return False
        dot_idx = base.index('.') if '.' in base else -1
        if dot_idx != -1:
            num1 = base[:dot_idx]
            num2 = base[dot_idx+1:]
        else:
            num1 = base
            num2 = ''
        flag, num1 = strip_sign(num1)
        if not flag: return False
        print(f"num1:{num1}, num2:{num2}, exp:{exp}")
        # deal with empty base
        if exp_idx != -1 and ((not num1 and not num2) or not exp):
            return False
        if not num1 and not num2 and not exp: return False
        return is_digits(num1) and is_digits(num2) and is_digits(exp)




su = Solution()



# case bug
s = "-e"
res = su.isNumber(s)
ans = False
assert(res == ans)

# case exp
s = "1e2000"
res = su.isNumber(s)
ans = True
assert(res == ans)

# case dot
s = "123.52e525"
res = su.isNumber(s)
ans = True
assert(res == ans)

# case dot False
s = "123.52.e525"
res = su.isNumber(s)
ans = False
assert(res == ans)

# case empty string

# case std1
s = "0"
res = su.isNumber(s)
ans = True
assert(res == ans)
# case std2
s = "e"
res = su.isNumber(s)
ans = False
assert(res == ans)
# case std3
s = "."
res = su.isNumber(s)
ans = False
assert(res == ans)