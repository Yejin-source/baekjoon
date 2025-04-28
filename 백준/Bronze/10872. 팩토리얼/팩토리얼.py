N = int(input())

result = 1
for i in range(1, N+1):  # 1부터 N까지 반복
    result = result * i  # result *= i
print(result)
      
      
# for문 
# for 변수 in 객체(리스트, 문자열 등):
    
# range() 함수 
# 특정 범위의 숫자 시퀀스를 만드는 함수

# range(stop)
# range(start, stop) 
# range(start, stop, step)

# start : 범위의 시작 값 | 기본값 0
# stop : 범위의 마지막 값 | 해당 값은 범위에 포함되지 않음
# step : 수의 간격 | 기본값 1