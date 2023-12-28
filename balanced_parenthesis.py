from stack import Stack

def is_balanced(expression: str) -> bool:
    """
    Return True if the expression is balanced, False otherwise.
    """

    stack = Stack() # Create a stack object
    for char in expression:
        if char in "({[":
            stack.push(char)
        elif char in ")}]":
            if stack.is_empty():
                return False  # Closing bracket without a corresponding opening bracket
            top = stack.pop()
            if not is_matching(top, char):
                return False  # Mismatched opening and closing brackets

    return stack.is_empty()


def is_matching(opening, closing):
    bracket_pairs = {"(": ")", "{": "}", "[": "]"}
    return bracket_pairs[opening] == closing


# Example usage:
expression1 = "{[()]}"
expression2 = "{[(])}"

print(f"Is balanced: {expression1} - {is_balanced(expression1)}")
print(f"Is balanced: {expression2} - {is_balanced(expression2)}")
