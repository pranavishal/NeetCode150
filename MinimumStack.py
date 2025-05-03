class MinStack:

    def __init__(self):
        self.theStack = []
        self.minVal = None
        

    def push(self, val: int) -> None:
        if len(self.theStack) == 0:
            self.minVal = val
        
        else:
            if val < self.minVal:
                self.minVal = val
        
        self.theStack.append((val, self.minVal))
        

    def pop(self) -> None:
        self.theStack.pop()
        if len(self.theStack) > 1:
            self.minVal = self.theStack[len(self.theStack) - 1][1]
        

    def top(self) -> int:
        return self.theStack[len(self.theStack) - 1][0]
        

    def getMin(self) -> int:
        return self.theStack[len(self.theStack) - 1][1]
        
