class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack=[]
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minStack:
            self.minStack.append(val)
        else:
            if self.minStack[-1] != None  and (val<=self.minStack[-1]):
                self.minStack.append(val)

    def pop(self) -> None:
        #val = self.top
        val = self.stack.pop()
        if self.minStack[-1] != None and (self.minStack[-1]==val):
            self.minStack.pop()


        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:

        return self.minStack[-1]
            


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()