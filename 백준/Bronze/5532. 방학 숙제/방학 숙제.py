L = int(input())  # 방학 일수
A = int(input())  # 국어 총 페이지
B = int(input())  # 수학 총 페이지
C = int(input())  # 하루에 풀 수 있는 국어 페이지
D = int(input())  # 하루에 풀 수 있는 수학 페이지

# 각 과목 숙제 일수 (올림 계산)
korean_days = (A+C-1) // C
math_days = (B+D-1) // D

# 놀 수 있는 날의 최댓값 출력
print(L - max(korean_days, math_days))