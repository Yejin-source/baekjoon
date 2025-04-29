N = int(input())

for i in range(1, N+1):  # 1부터 N까지 N회 반복
    star = "*" * i  # i개 만큼 별 문자열 생성
    print(star)


# 변수 없이 출력
# for i in range(1, N+1):
#    "*" * i
#    print("*" * i)