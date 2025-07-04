import sys

# 수의 개수
N = int(sys.stdin.readline())

# 수의 범위: 1 ~ 10000 -> 10001개 리스트 생성
count = [0] * 10001

# 각 수의 등장 횟수 카운팅
for _ in range(N):
    num = int(sys.stdin.readline())
    count[num] += 1

# 정렬된 순서로 수를 등장 횟수만큼 출력
for i in range(1, 10001):
    if count[i] > 0:
        for _ in range(count[i]):
            print(i)