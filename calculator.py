def to_tokens(s):
    for i in '+-*/()=':
        s = s.replace(i, ' % s ' % i)
    return s.split()


PREC = {
    '-': 1,
    '+': 1,
    '*': 2,
    '/': 2
}


def ishigher(x, y):
    return x in PREC and PREC[x] >= PREC[y]


def to_rpn(tokens):
    stack = []
    result = []

    if tokens[0] == '-':
        del tokens[0]
        tokens[0] = '-' + tokens[0]

    for i in tokens:
        if i in PREC:
            while stack and ishigher(stack[-1], i):
                result.append(stack.pop())
            stack.append(i)
        elif i == '(':
            stack.append(i)
        elif i == ')':
            while stack[-1] != '(':
                result.append(stack.pop())
            stack.pop()
        else:
            result.append(i)
    while stack:
        result.append(stack.pop())
    return result


def calculator(rpn):
    rpn = to_tokens(rpn)
    rpn = to_rpn(rpn)
    stack = []
    for i in rpn:
        if i == '+':
            stack.append(stack.pop() + stack.pop())
        elif i == '-':
            stack.append(-1 * stack.pop() + stack.pop())
        elif i == '*':
            stack.append(stack.pop() * stack.pop())
        elif i == '/':
            stack.append(1 / stack.pop() * stack.pop())
        else:
            stack.append(float(i))
    if len(stack) == 1:
        return int(stack[0])


if __name__ == '__main__':
    print(calculator(input()))
