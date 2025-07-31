# 시간 초과 발생: input() -> sys.stdin.readline()
import sys
input = sys.stdin.readline

# 명령의 수
N = int(input())

# 스택 초기화
stack = []

for _ in range(N):
    command = input().split()  # 명령 입력 | 스택 문제에서 자주 쓰는 변수명

    if command[0] == '1':  # push
        stack.append(int(command[1]))

    elif command[0] == '2':  # pop
        print(stack.pop() if stack else -1)  # pop(): 마지막 요소 제거 후 반환

    elif command[0] == '3':  # size
        print(len(stack))

    elif command[0] == '4':  # empty
        print(1 if not stack else 0)

    elif command[0] == '5':  # top
        print(stack[-1] if stack else -1)  # 마지막 요소 확인