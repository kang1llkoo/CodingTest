def solution(binomial):
    num1, op, num2 = binomial.split(' ')
    if op == '+':
        return int(num1) + int(num2)
    elif op == '-':
        return int(num1) - int(num2)
    elif op == '*':
        return int(num1) * int(num2)