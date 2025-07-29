# 통화 횟수
N = int(input())

# 통화 시간 리스트
times = list(map(int, input().split()))


Y = 0  # 영식 요금제
M = 0  # 민식 요금제

for t in times:
    Y += (t // 30 + 1) * 10  # 30초마다 10원
    M += (t // 60 + 1) * 15  # 60초마다 15원

# 저렴한 요금제 출력
if Y < M:
    print('Y', Y)
elif M < Y:
    print('M', M)
else:
    print('Y M', Y)