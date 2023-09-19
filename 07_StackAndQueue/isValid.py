def isValid(s):
    stack = []
    for char in s:
        if char == '(' or char == '[' or char == '{':
            stack.append(char)
        elif char == ')':
            if len(stack) == 0 or stack.pop() != '(':
                return False
        elif char == ']':
            if len(stack) == 0 or stack.pop() != '[':
                return False
        elif char == '}':
            if len(stack) == 0 or stack.pop() != '{':
                return False
    return len(stack) == 0

if __name__ == "__main__":
    print(isValid("()[]{}"))