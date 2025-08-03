import sys
input = sys.stdin.readline

# 멀티탭의 개수
N = int(input())

total = 0

# 각 멀티탭의 사용 가능한 콘센트 수 누적
for _ in range(N):
    sockets = int(input()) - 1  # 하나는 멀티탭 본인이 사용
    total += sockets

# 마지막 멀티탭은 본인 연결 불필요 -> +1
print(total + 1)