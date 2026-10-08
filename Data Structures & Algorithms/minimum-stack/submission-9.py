class MinStack:

    def __init__(self):
        self.min = float('inf')
        self.stack = []

    def push(self, val: int) -> None:
        # val - min
        self.stack.append(val - self.min if self.stack else 0)
        self.min = min(self.min, val)

    def pop(self) -> None:
        if not self.stack:
            return
        
        val = self.stack.pop()

        if val < 0:
            # need to find old min
            # val = current_min - old min
            self.min = self.min - val
        
        if not self.stack:
            self.min = float('inf')

    def top(self) -> int:
        if not self.stack:
            return -1
        
        val = self.stack[-1]

        if val < 0:
            return self.min
        else:
            # val = actual_val - self.min
            return val + self.min
        

    def getMin(self) -> int:
        return self.min
