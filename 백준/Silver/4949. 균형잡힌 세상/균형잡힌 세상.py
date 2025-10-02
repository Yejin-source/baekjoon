while True:
    sentence = input()

    if sentence == '.':  # 입력 종료 조건
        break

    stack = []

    for ch in sentence:
        if ch == '(' or ch == '[':  # 여는 괄호 push
            stack.append(ch)

        elif ch == ')':           # 닫는 소괄호
            if stack and stack[-1] == '(':
                stack.pop()       # 짝을 이루는 경우 pop
            else:
                stack.append(ch)  # 에러 표시용 push
                break

        elif ch == ']':           # 닫는 대괄호
            if stack and stack[-1] == '[':
                stack.pop()       # 짝을 이루는 경우 pop
            else:
                stack.append(ch)  # 에러 표시용 push
                break

    if not stack:  # 빈 스택 -> 균형잡힌 문자열
        print('yes')
    else:
        print('no')