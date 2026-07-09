class MinStack:

    def __init__(self):
        self.stack = []
        self.mini = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.mini.append(min(self.mini[-1] if len(self.mini) else float('inf'), val))
        
    def pop(self) -> None:
        if len(self.mini):
            self.mini.pop()
            return self.stack.pop()
        return None


    def top(self) -> int:
        return self.stack[-1] if len(self.stack) else None

    def getMin(self) -> int:
        return self.mini[-1] if len(self.mini) else None
