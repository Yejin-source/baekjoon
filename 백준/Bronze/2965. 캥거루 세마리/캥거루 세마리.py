# 세 캥거루 초기 위치
A, B, C = map(int, input().split())

# 두 간격 중 더 넓은 쪽에서 한 칸만 남을 때까지 이동
# 움직일 수 있는 최대 횟수 출력
print(max(B-A, C-B) - 1)