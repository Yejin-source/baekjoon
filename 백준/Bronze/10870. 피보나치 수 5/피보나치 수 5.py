# 재귀 함수로 피보나치 수 계산

def fibonacci(n):
    if n == 0:
        return 0  # 0번째 피보나치 수는 0
    
    elif n == 1:
        return 1  # 1번째 피보나치 수는 1
    
    return fibonacci(n-1) + fibonacci(n-2)  # n번째 = (n-1) + (n-2)

# 입력값을 바로 함수에 넣어 계산
print(fibonacci(int(input())))


# 재귀 함수는 종료 조건이 없으면 무한 반복됨
# -> 반드시 종료 조건이 필요함