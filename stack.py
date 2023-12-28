class stack:
    ''' Stack implementation using list'''
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def size(self):
        return len(self.items)
    
    def isEmpty(self):
        return self.items == 0
    
if __name__ == '__main__':
    stack = stack()