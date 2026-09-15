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
        
        # 3 -> min=3 (0)
        # 3 1 -> min=1 (0, -2)

        # 3 -> (0) -> min=3
        # 3 4 -> (0, 1) -> min=3
        # pop
        # to obtain 1, we do 

        popped = self.stack.pop()

        if popped < 0:
            self.min = self.min - popped

    def top(self) -> int:
        back = self.stack[-1]

        if back < 0:
            return self.min
        else:
            return self.min + back
        

    def getMin(self) -> int:
        return self.min
        
