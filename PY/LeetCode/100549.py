from typing import List

class Solution:
    def calculateScore(self, instructions: List[str], values: List[int]) -> int:
        i = 0
        score = 0
        visited = set()
        while 0 <= i < len(instructions):
            if i in visited: break
            visited.add(i)
            if instructions[i] == "add":
                score += values[i]
                i += 1
            elif instructions[i] == "jump":
                i += values[i]
            # print("score:",score)

        print(score)
        return score

su = Solution()
# case std1
instructions = ["jump","add","add","jump","add","jump"]
values = [2,1,3,1,-2,-3]
res = su.calculateScore(instructions, values)
ans = 1
assert(res == ans)

# case std2
instructions = ["jump","add","add"]
values = [3,1,1]
res = su.calculateScore(instructions, values)
ans = 0
assert(res == ans)
