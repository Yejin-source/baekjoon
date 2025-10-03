from collections import deque
import sys

input = sys.stdin.readline

N = int(input())
que = deque()  # 양쪽 끝에서 입출력이 가능한 큐

for _ in range(N):
    cmd = input().split()

    if cmd[0] == 'push':
        que.append(cmd[1])

    elif cmd[0] == 'pop':
        print(que.popleft() if que else -1)  # popleft(): 큐의 맨 앞 원소 제거

    elif cmd[0] == 'size':
        print(len(que))

    elif cmd[0] == 'empty':
        print(0 if que else 1)

    elif cmd[0] == 'front':
        print(que[0] if que else -1)

    elif cmd[0] == 'back':
        print(que[-1] if que else -1)