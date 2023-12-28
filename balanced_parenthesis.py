from stack import Stack

def is_balanced(expression: str) -> bool:
    """
    Return True if the expression is balanced, False otherwise.
    """
    stack1 = Stack()

    for char in expression:
        if char == '(':
            stack1.push(char)
        elif char == ')':
            if stack1.isEmpty():
                return False
            stack1.pop()

            top = stack1.pop()
            if top != '(':
                return False
    
    return stack1.isEmpty()

if __name__ == '__main__':
    expression1 = '(()()()())'
    print(is_balanced(expression1))