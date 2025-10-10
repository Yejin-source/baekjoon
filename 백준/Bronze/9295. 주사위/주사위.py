T = int(input())  # 테스트 케이스 수

for i in range(1, T+1):
    a, b = map(int, input().split())  # 두 주사위 값
    
    # f-string 사용: "Case i: 합" 출력
    print(f"Case {i}: {a + b}")