score = 0.0  # 총 점수 (누적합)
total_credit = 0.0  # 총 학점

# 등급별 점수를 딕셔너리로 정의
grade_dict = {
    'A+': 4.5, 'A0': 4.0,
    'B+': 3.5, 'B0': 3.0,
    'C+': 2.5, 'C0': 2.0,
    'D+': 1.5, 'D0': 1.0,
    'F': 0.0
}

# 20번 반복
for _ in range(20):
    # 과목명, 학점, 등급으로 구분
    subject, credit, grade = input().split()
    credit = float(credit)  # 학점을 실수형으로 반환

    # 'P' 등급은 계산에서 제외
    if grade != 'P':
        score += credit * grade_dict[grade]  # 학점 x 점수 누적
        total_credit += credit               # 학점 누적

# 최종 평점
print(score / total_credit)