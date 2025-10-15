import datetime

# D: 일, M: 월
D, M = map(int, input().split())

# 2009년 M월 D일 날짜 객체 생성
date = datetime.date(2009, M, D)

# weekday(): 0=월요일, 6=일요일 반환
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# 요일 출력
print(weekdays[date.weekday()])