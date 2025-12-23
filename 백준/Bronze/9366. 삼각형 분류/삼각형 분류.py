T = int(input())  # 테스트 케이스 수

for i in range(1, T+1):
    A, B, C = map(int, input().split())  # 세 변
    a, b, c = sorted([A, B, C])

    if a + b <= c:
        type = 'invalid!'
    elif a == b == c:
        type = 'equilateral'
    elif a == b or b == c:
        type = 'isosceles'
    else:
        type = 'scalene'

    print(f"Case #{i}: {type}")