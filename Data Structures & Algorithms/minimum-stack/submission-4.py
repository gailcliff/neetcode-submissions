class MinStack:

    def __init__(self):
        self.stack = []
        self.min = float('inf')
        

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(0)
            self.min = val
        else:
            self.stack.append(val - self.min)
            self.min = min(self.min, val)
        

    def pop(self) -> None:
        if not self.stack:
            return
        
        popped = self.stack.pop()

        if popped < 0:
            self.min = self.min - popped
        

    def top(self) -> int:
        if not self.stack:
            return float('inf')
        
        back = self.stack[-1]

        if back < 0:
            return self.min
        else:
            return back + self.min
        

    def getMin(self) -> int:
        return self.min
        
