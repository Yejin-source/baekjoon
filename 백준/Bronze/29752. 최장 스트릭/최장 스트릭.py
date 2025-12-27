N = int(input())                     # 기간(일 수)
S = list(map(int, input().split()))  # 각 날짜에 푼 문제 수

streak = 0
max_streak = 0

for x in S:
    if x > 0:
        streak += 1
        if streak > max_streak:
            max_streak = streak
    else:
        streak = 0

print(max_streak)  # 최장 스트릭