class Stack:
    def __init__(self):
        self.stack = []
    
    def insert(self, val):
        self.stack.insert(0, val)
    
    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop(0)
        return None
    
    def top(self):
        if len(self.stack) > 0:
            return self.stack[0]
        else:
            return None
    
    def empty(self):
        return len(self.stack) == 0


def is_valid(i, j):
    if i == '[':
        return j == ']'
    
    if i == '{':
        return j == '}'
    
    if i == '(':
        return j == ')'
    
    return False

def isValid(s):
    stack = Stack()

    for i in s:
        top = stack.top()
        if is_valid(i, top) or is_valid(top, i):
            stack.pop()
            continue
        
        stack.insert(i)
    
    return stack.empty()

print(isValid('[({){}]'))