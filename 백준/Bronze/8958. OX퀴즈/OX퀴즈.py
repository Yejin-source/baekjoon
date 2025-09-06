# 테스트 케이스 개수
T = int(input())

for _ in range(T):
    result = input()
    score = 0  # 연속된 O의 누적 점수
    total = 0  # 전체 합계 점수

    for ch in result:
        if ch == 'O':  # O이 연속되는 경우
            score += 1
            total += score
        else:
            score = 0   # X 나오면 초기화

    print(total)