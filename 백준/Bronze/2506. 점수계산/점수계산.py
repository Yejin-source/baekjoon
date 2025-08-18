# 문제 개수
N = int(input())

# 채점 결과
answers = list(map(int, input().split()))

score = 0  # 총 점수
count = 0  # 연속 정답 개수

for ans in answers:
    if ans == 1:       # 정답일 때
        count += 1
        score += count
    else:              # 오답일 때
        count = 0

print(score)