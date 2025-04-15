class MinStack:

    def __init__(self):
        self.stack = []
        self.min = []
    
    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min or val < self.min[-1][0] :
            self.min.append([val,1])
        else : # if val == self.min[-1][0] :
            self.min[-1][1] += 1

    # def push(self, val: int) -> None:
    #     self.stack.append(val)
    #     if not self.min or val <= self.min[-1] :
    #         self.min.append(val)
    #     else :
    #         self.min.append(self.min[-1])

    def pop(self) -> None:
        self.min[-1][1] -= 1
        
        if self.min[-1][1] == 0 :
            self.min.pop()

        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min[-1][0]
    

su = MinStack()
su.push(3)
print(su.getMin())
su.push(4)
print(su.getMin())
su.push(5)
print(su.getMin())
print(su.min)
su.pop()
print(su.getMin())
su.push()