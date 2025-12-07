# L: 왼발잡이 수, R: 오른발잡이 수, A: 양발잡이 수
L, R, A = map(int, input().split())

diff = abs(L-R)  # L, R 인원 차이

# A로 인원 차이 보완
if A >= diff:
    A -= diff
    L = R = max(L, R)
else:
    # A가 부족한 경우
    if L < R:
        L += A
    else:
        R += A
    A = 0

# 남은 A는 쌍으로 추가
L += A // 2
R += A // 2

print(min(L, R) * 2)  # 최대 잔류 인원