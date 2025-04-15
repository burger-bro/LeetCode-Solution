from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        print("********* start **********")
        stack = []
        def div(a, b):
            v = abs(a) // abs(b)
            return v if a * b > 0 else -v
        op_dict = {'+': lambda a,b: a+b,
                   '-': lambda a,b: a-b,
                   '*': lambda a,b: a*b,
                   '/': lambda a,b: int(a/b),
                #    '/': div
                   }
        for t in tokens:
            print(stack)
            if t in op_dict:
                op2 = stack.pop()
                op1 = stack.pop()
                stack.append(op_dict[t](op1, op2))
            else:
                stack.append(int(t))
        print("ret:", stack[0])
        return stack[0]


su = Solution()

# case std1
tokens = ["2","1","+","3","*"]
res = su.evalRPN(tokens)
ans = 9
assert(res == ans)

# case std2
tokens = ["4","13","5","/","+"]
res = su.evalRPN(tokens)
ans = 6
assert(res == ans)

# case std3
tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
res = su.evalRPN(tokens)
ans = 22
assert(res == ans)


