class Stack:
    ''' Stack implementation using list'''
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if self.is_empty():
            return None  # Return None if stack is empty
        return self.items.pop()
    
    def size(self):
        return len(self.items)
    
    def is_empty(self):
        return self.items == []
    
    