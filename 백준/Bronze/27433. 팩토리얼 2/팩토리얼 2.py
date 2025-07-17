# 재귀 함수로 팩토리얼 계산

def factorial(n):
    if n == 0:                 # 종료 조건: 0! = 1
        return 1
    
    return n * factorial(n-1)  # 재귀 호출: n * (n-1)!

# 입력값을 바로 함수에 넣어 계산
print(factorial(int(input())))