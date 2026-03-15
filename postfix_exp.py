import math

def evaluatePostfix(arr):

    stack = []

    for token in arr:

        if token not in "+-*/^":
            stack.append(int(token))

        else:
            b = stack.pop()
            a = stack.pop()

            if token == '+':
                stack.append(a + b)

            elif token == '-':
                stack.append(a - b)

            elif token == '*':
                stack.append(a * b)

            elif token == '/':
                stack.append(a // b)

            elif token == '^':
                stack.append(a ** b)

    return stack.pop()
arr = ["2","3","1","*","+","9","-"]

print(evaluatePostfix(arr))