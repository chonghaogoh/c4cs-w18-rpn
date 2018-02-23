#!/usr/bin/env python

def calculate(arg):
    stack = list()
    for token in arg.split():
        try:
            value = int(token)
            stack.append(value)
        except ValueError:
            if token == '+':
                arg2 = stack.pop()
                arg1 = stack.pop()
                result = arg1 + arg2
                stack.append(result)
            elif token == '-':
                arg2 = stack.pop()
                arg1 = stack.pop()
                result = arg1 - arg2 
                stack.append(result)
            else:
                print("not implemented yet")
        print(stack)
    return stack.pop()

def main():
    while True:
        print(calculate(input('rpn calc> ')))

if __name__ == '__main__':
    main()