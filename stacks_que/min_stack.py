class MinStack:
    def __init__(self):
        self.stack = []
    
    def push(self, x):
        
        if len(self.stack) == 0:
            self.stack.append((x, x))
            return
        
        currentMin = self.stack[len(self.stack)-1][1]

        if x < currentMin:
            currentMin = x
        
        self.stack.append((x, currentMin))
        return
    
    def pop(self):
        return self.stack.pop()
    
    def top(self):
        return self.stack[len(self.stack)-1][0]
    
    def getMin(self):
        return self.stack[len(self.stack)-1][1]
