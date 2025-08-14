# N: 총 노래 수, L: 모든 노래 길이, D: 전화벨 간격
N, L, D = map(int, input().split())

total_time = N * L + (N - 1) * 5  # 전체 노래 재생 시간
bell = 0  # 벨이 울리는 시간

while True:
    # 공백 구간이거나 모든 노래가 끝난 경우
    if bell % (L + 5) >= L or bell >= total_time:
        print(bell)
        break
    bell += D