# 손님 수
N = int(input())

# 손님들이 원하는 자리 번호
visitors = list(map(int, input().split()))

seated = set()  # 이미 사람이 앉은 자리
reject = 0    # 거절당한 손님 수

for v in visitors:
    if v in seated:    # 이미 사람이 앉아 있다면
        reject += 1
    else:
        seated.add(v)  # 빈 자리에 앉기

print(reject)