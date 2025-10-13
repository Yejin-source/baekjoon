n = int(input())  # 라운드 수
a_score, b_score = 100, 100  # 초기 점수 (각 100점)

for _ in range(n):
    a, b = map(int, input().split())  # 각 사람이 던진 주사위 눈
    
    # 점수 계산
    if a > b:
        b_score -= a
    elif a < b:
        a_score -= b

# 최종 점수 출력
print(a_score)
print(b_score)