scores = []  # 각 참가자 총점 리스트

for _ in range(5):
    scores.append(sum(map(int, input().split())))

max_score = max(scores)               # 우승자 점수
winner = scores.index(max_score) + 1  # 우승자 번호

print(winner, max_score)