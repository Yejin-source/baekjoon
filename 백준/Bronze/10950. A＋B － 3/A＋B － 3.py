T = int(input()) # 테스트 케이스 개수

# for문을 T번 반복
for i in range(1, T+1):
    A, B = map(int, input().split())  # 반복할 때마다 새로운 A, B 입력받기
    print(A+B)
    

# range(stop)
# range(start, stop) 
# range(start, stop, step)

# start : 범위의 시작 값 | 기본값 0
# stop : 범위의 마지막 값 | 해당 값은 범위에 포함되지 않음
# step : 수의 간격 | 기본값 1