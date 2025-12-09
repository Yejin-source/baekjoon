result = int(input())  # 첫 번째 숫자

while True:
    op = input()  # 연산자 또는 '='

    if op == '=':
        print(result)
        break

    num = int(input())  # 다음 숫자

    if op == '+':
        result += num
    elif op == '-':
        result -= num
    elif op == '*':
        result *= num
    elif op == '/':
        result //= num