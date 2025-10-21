n = int(input())  # 정수

while True:
    x = int(input())  # 수 목록
    
    if x == 0:  # 종료 조건
        break
    
    if x % n == 0:  # n의 배수 여부 출력
        print(f"{x} is a multiple of {n}.")
    else:
        print(f"{x} is NOT a multiple of {n}.")