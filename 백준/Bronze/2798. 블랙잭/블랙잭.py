# N: 카드 개수, M: 목표 합
N, M = map(int, input().split())

# 카드에 적힌 숫자들
cards = list(map(int, input().split()))

# 최대 합 저장
max_total = 0


# 서로 다른 3장의 카드 조합 확인
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            
            # 3장의 카드 합 계산
            total = cards[i] + cards[j] + cards[k]
            
            # M을 넘지 않으면
            if total <= M:
                # 최대값 갱신
                max_total = max(max_total, total)

# 최대 카드 합 출력
print(max_total)