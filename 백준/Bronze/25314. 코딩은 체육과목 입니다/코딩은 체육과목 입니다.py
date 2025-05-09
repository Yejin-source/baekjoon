# N바이트 정수 (4의 배수)
N = int(input())

# N을 4로 나눈 만큼 반복
for _ in range(N // 4):
    print("long", end=" ") # 줄바꿈 없이 공백 추가

# 마지막에 "int" 출력
print("int")