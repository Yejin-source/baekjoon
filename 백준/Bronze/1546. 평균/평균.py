# 시험 본 과목의 개수
N = int(input())

# 점수
scores = list(map(int, input().split()))

# 최고 점수
M = max(scores)


# N번 반복
for i in range(N):
    scores[i] = scores[i]/M*100

# 새로운 평균 출력
print(sum(scores)/N)