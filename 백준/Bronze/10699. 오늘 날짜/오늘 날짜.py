from datetime import datetime as dt

print(dt.now().strftime("%Y-%m-%d"))

# datetime.now() : 현재 지역 시간의 날짜 및 시간
# datetime.strftime() : 특정 포맷으로 출력
# %Y : YYYY  vs  %y : YY