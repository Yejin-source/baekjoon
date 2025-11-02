A, B = map(int, input().split())  # 두 통장의 잔고
C = int(input())                  # 치킨 한 마리 가격

if (A+B) >= 2*C:
    # 두 마리 사고 남은 잔고 출력
    print(A+B - 2*C)  
else:
    # 사지 못하면 현재 잔고 출력
    print(A+B)