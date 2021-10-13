PREC = {
    '-': 1,
    '+': 1,
    '*': 2,
    '/': 2
}


def to_tokens(expression):
    for i in '+-*/()=':
        expression = expression.replace(i, ' % s ' % i)
    expression = expression.split()
    count = 0
    signs = '+-*/(='
    while count < len(expression) - 1:
        if expression[0] == '-':
            expression.pop(0)
            expression[0] = '-' + expression[0]
            continue
        if expression[count] == '-' and expression[count-1] in signs:
            expression.pop(count)
            expression[count] = '-' + expression[count]
            continue
        count += 1
    return expression


def ishigher(x, y):
    return x in PREC and PREC[x] >= PREC[y]


def to_rpn(tokens):
    stack = []
    result = []
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
