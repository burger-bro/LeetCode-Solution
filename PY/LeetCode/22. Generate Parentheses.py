from typing import List

class Solution:
    def generateParenthesis0(self, n: int) -> List[str]:
        answer = []
        def solve(left, right, parenthesis):
            print(left, right)
            if left == 0 and right == 0:
                if self.isvalid(parenthesis):
                    print(left, right, parenthesis)
                    answer.append(parenthesis)
            left-1 >= 0 and solve(left-1, right, parenthesis+'(')
            right-1 >= 0 and solve(left, right-1, parenthesis+')')

        solve(n, n, "")
        print(answer)
        return answer

    def isvalid(self, parenthsis):
        stack_cnt = 0
        for c in parenthsis:
            if stack_cnt < 0:
                return False
            if c == '(':
                stack_cnt += 1
            else:
                stack_cnt -= 1
        return True

    def generateParenthesis(self, n: int) -> List[str]:
        answer = []
        def solve(left, right, parenthesis):
            if len(parenthesis) == 2*n:
                # print(left, right, parenthesis)
                answer.append(parenthesis)
            left > 0 and solve(left-1, right, parenthesis+'(')
            right > left and solve(left, right-1, parenthesis+')')

        solve(n, n, "")
        # print(answer)
        return answer

su = Solution()
n = 3
ans = ["((()))","(()())","(())()","()(())","()()()"]
res = su.generateParenthesis(n)
assert(ans == res)

n = 1
ans = ["()"]
res = su.generateParenthesis(n)
assert(ans == res)
