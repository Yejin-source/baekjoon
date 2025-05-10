# 테스트 케이스의 개수
T = int(input())

# 1부터 T까지 T번 반복
for x in range(1, T+1):
    A, B = map(int, input().split())

    C = A + B
    print(f"Case #{x}: {A} + {B} = {C}")  # f-string 사용


# f-string
# f"문자열 {표현식} 문자열"