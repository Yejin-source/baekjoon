# 테스트 데이터의 수
T = int(input())

for _ in range(T):
    count = 0  # 괄호 개수 차이 저장
    ps = input()

    for char in ps:
        if count < 0:  # 닫는 괄호가 더 많아지면 VPS가 아님
            break      # 반복 종료

        if char == '(':
            count += 1  # 여는 괄호일 때 +1
        else:
            count -= 1  # 닫는 괄호일 때 -1

    print('YES' if count == 0 else 'NO')