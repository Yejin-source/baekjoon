month = int(input())  # 월
day = int(input())    # 해당 달의 날짜 

# 2월 18일과 비교 후 출력
if month < 2 or (month == 2 and day < 18):  # 이전 날짜
    print("Before")
elif month == 2 and day == 18:              # 같은 날짜
    print("Special")
else:                                       # 이후 날짜
    print("After")