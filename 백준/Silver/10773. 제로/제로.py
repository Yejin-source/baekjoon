import sys
input = sys.stdin.readline

# 입력 개수
K = int(input())

# 스택 초기화
stack = []

for _ in range(K):
    cmd = int(input())  # 명령어 입력

    if cmd == 0:  # 정수가 0일 경우 최근 수 제거
        stack.pop()
    else:         # 0이 아닐 경우 스택에 추가
        stack.append(cmd)

# 최종적으로 스택에 남아있는 수의 합 출력
print(sum(stack))